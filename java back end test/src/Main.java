// Press Shift twice to open the Search Everywhere dialog and type `show whitespaces`,
// then press Enter. You can now see whitespace characters in your code.

//json and io imports for writing to Json
import org.json.*;
import java.io.FileWriter;
import java.io.IOException;

//periodically reading Json
import java.lang.reflect.Array;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.*;
import java.util.concurrent.Executors;
import java.util.concurrent.ScheduledExecutorService;
import java.util.concurrent.TimeUnit;

public class Main {
    public static void main(String[] args) {
        writeToJson("NONE");

        String filePath = "C:/Users/dieks/IdeaProjects/JSONTEST/python-output.json";
        long interval = 1000; // 1 second

        ScheduledExecutorService executorService = Executors.newSingleThreadScheduledExecutor();
        executorService.scheduleAtFixedRate(() -> listenToJson(filePath), 0, interval, TimeUnit.MILLISECONDS);
    }

    public static void listenToJson (String filePath) {
        try {
            byte[] fileBytes = Files.readAllBytes(Paths.get(filePath));
            String fileContent = new String(fileBytes);
            //process JSON contents
            JSONObject obj = new JSONObject(fileContent);
            JSONArray jsonArray = obj.getJSONArray("move");

            ArrayList<Integer> movesXY = new ArrayList<>();
            for (int i = 0; i < jsonArray.length(); i++) {
                int element = jsonArray.getInt(i);
                movesXY.add(element);
            }

            if (validateMove(movesXY)) {
                writeToJson("ALLOWED");
                clearLocalJSON();
            }


            System.out.println(fileContent);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static void writeToJson (String status) {
        //Creating a JSONObject object
        JSONObject jsonObject = new JSONObject();
        //Inserting key-value pairs into the json object
        jsonObject.put("move-status", status);
        try {
            FileWriter file = new FileWriter("F:/Documents/GitHub/bagel-blitz-front-end/java-output.json");
            file.write(jsonObject.toString());
            file.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
        System.out.println("JSON file created: "+jsonObject);
    }

    public static boolean validateMove (ArrayList<Integer> movesXY) {
        if (movesXY.get(0) != -1 && movesXY.get(1) != -1) {
            return true;
        }
        return false;
    }

    public static void clearLocalJSON () {
        JSONObject jsonObject = new JSONObject();

        jsonObject.put("move", List.of(-1 , -1));

        try {
            FileWriter file = new FileWriter("C:/Users/dieks/IdeaProjects/JSONTEST/python-output.json");
            file.write(jsonObject.toString());
            file.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
        System.out.println("JSON file created: "+jsonObject);
    }
}