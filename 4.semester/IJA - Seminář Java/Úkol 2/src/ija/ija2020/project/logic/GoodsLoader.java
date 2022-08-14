package ija.ija2020.project.logic;

import ija.ija2020.project.warehouse.Warehouse;
import ija.ija2020.project.warehouse.Item;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

/***
 * Class that loads given warehouse with goods (goods are represented as text input in file)
 * Author: Marián Zimmerman, xzimme03
 */

public class GoodsLoader {
    /***
     *
     * @param path Path to file with input data
     * @param warehouse Warehouse which will be filled
     */

    public void loadGoods(String path, Warehouse warehouse){
        try {
            File myObj = new File(path);
            Scanner myReader = new Scanner(myObj);
            while (myReader.hasNextLine()) {
                String data = myReader.nextLine();
                String[] split = data.split("\\s+");
                String itemType = split[0];
                int amount = Integer.parseInt(split[1]);
                for (int i = 0; i < amount; i++){
                    Item item = new Item(itemType);
                    warehouse.addItem(item);
                }

            }

            myReader.close();
        }
        catch (FileNotFoundException e)  {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }
    }
}
