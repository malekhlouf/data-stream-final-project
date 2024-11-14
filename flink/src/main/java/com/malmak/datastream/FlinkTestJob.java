package com.malmak.datastream;

import org.apache.flink.api.java.tuple.Tuple2;
import org.apache.flink.streaming.api.environment.StreamExecutionEnvironment;
import org.apache.flink.streaming.api.datastream.DataStream;

public class FlinkTestJob {

    public static void main(String[] args) throws Exception {
        // Set up the execution environment
        StreamExecutionEnvironment env = StreamExecutionEnvironment.getExecutionEnvironment();

        // Create a simple stream with some data
        DataStream<Tuple2<String, Integer>> text = env.fromElements(
            Tuple2.of("Hello", 1),
            Tuple2.of("Flink", 2),
            Tuple2.of("Streaming", 3)
        );

        // Print the data to the console
        text.print();

        // Execute the job
        env.execute("Flink Test Job");
    }
}