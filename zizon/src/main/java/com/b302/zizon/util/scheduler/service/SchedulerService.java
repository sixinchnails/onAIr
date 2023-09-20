package com.b302.zizon.util.scheduler.service;

import com.b302.zizon.domain.live.entity.LiveQueue;
import com.b302.zizon.domain.live.repository.LiveQueueRepository;
import com.b302.zizon.domain.oncast.entity.Oncast;
import com.b302.zizon.domain.oncast.repository.OncastRepository;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Service;

import javax.transaction.Transactional;
import java.util.Collections;
import java.util.List;

@Service
@RequiredArgsConstructor
@Slf4j
public class SchedulerService {

    private final OncastRepository oncastRepository;
    private final LiveQueueRepository liveQueueRepository;

    // 채택하기 라이브큐
    @Scheduled(cron = "0 48 13 * * *", zone = "Asia/Seoul")
    @Transactional
    public void selectedOncast(){
        log.info("라이브큐 채택 스케줄러 동작");
        List<Oncast> byOncast = oncastRepository.findByDeleteCheckFalseAndSelectCheckFalseAndShareCheckTrue();
        Collections.shuffle(byOncast);
        // 공유 상태가 10개를 넘은 경우
        if(byOncast.size() > 10){
            // 섞고
            int count = 0;
            for(Oncast oncast : byOncast){
                if(count >= 10){
                    break;
                }
                oncast.updateSeletedOncast();
                LiveQueue build = LiveQueue.builder()
                        .oncast(oncast)
                        .user(oncast.getUser())
                        .build();
                liveQueueRepository.save(build);

                count++;
            }
        }else{
            for(Oncast oncast : byOncast){
                oncast.updateSeletedOncast();
                LiveQueue build = LiveQueue.builder()
                        .oncast(oncast)
                        .user(oncast.getUser())
                        .build();
                liveQueueRepository.save(build);
            }
        }
    }

    // 라이브큐에 있는 내용 삭제하기
    @Scheduled(cron = "0 0 23 * * *", zone = "Asia/Seoul")
    @Transactional
    public void deleteLiveQueue(){
        log.info("라이브큐 삭제 스케줄러 동작");
        List<LiveQueue> byLiveQueue = liveQueueRepository.findAll();
        for(LiveQueue q : byLiveQueue){
            liveQueueRepository.delete(q);
        }
    }
}