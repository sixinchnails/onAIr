from transformers import XLMRobertaConfig, XLMRobertaForSequenceClassification, XLMRobertaTokenizer
import torch, configparser
import sentencepiece as spm

config = configparser.ConfigParser()
config.read('config.ini')

directory = config['MODEL']['directory']

def vad_calculate(sentence):
    output_model_file = directory + "pytorch_model.bin"
    output_config_file = directory + "config.json"
    output_vocab_file = directory + "vocab.txt"

    config = XLMRobertaConfig.from_json_file(output_config_file)
    model = XLMRobertaForSequenceClassification(config)
    state_dict = torch.load(output_model_file, map_location=torch.device('cpu'))
    model.load_state_dict(state_dict, strict=False)
    tokenizer = XLMRobertaTokenizer.from_pretrained("xlm-roberta-base")

    # Tokenize the input
    inputs = tokenizer.encode_plus(sentence, add_special_tokens=True, return_tensors="pt", truncation=True,
                                   padding=True)

    result = model.forward(inputs['input_ids'], inputs['attention_mask'])

    # Apply softmax to get probabilities
    probabilities = torch.nn.functional.sigmoid(result.logits)

    # Convert probabilities to numpy array

    return probabilities[0][0].item(), probabilities[0][1].item()
