import dataGrabbers.*;
import java.util.*;

public class GtfsMain {

    public static void main(String[] args) throws Exception{
        Scanner reader = new Scanner(System.in);  // Reading from System.in
        System.out.println("Enter a stop: ");
        String stop = reader.nextLine();
        reader.close();
        StopData.get(stop);
    }


}