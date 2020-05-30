package com.app;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.boot.CommandLineRunner;

@ComponentScan("com.app")
@SpringBootApplication
public class ApacheDerbyExample implements CommandLineRunner {
 
    public static void main(String[] args) {
        System.out.println("STARTING THE APPLICATION");
        SpringApplication.run(ApacheDerbyExample.class, args);
        System.out.println("APPLICATION FINISHED");
    }
  
    @Override
    public void run(String... args) {
        System.out.println("EXECUTING : command line runner");
        //org.apache.derby.jdbc.ClientDataSource ds = new org.apache.derby.jdbc.ClientDataSource();
        //ds.setDatabaseName("mydb");
    }
}
