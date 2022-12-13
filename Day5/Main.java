package Day4;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class Main {

    public Main() {
        try {
            BufferedReader reader = new BufferedReader(new FileReader("input.txt"));
            String line = reader.readLine();
            while (line != null) {
                System.out.println(line);
                line = reader.readLine();
            }

            reader.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static void main(String... vargs) {
        new Main();
    }

}
