package ija.ija2020.project.logic;

import ija.ija2020.project.warehouse.Warehouse;
import ija.ija2020.project.warehouse.Item;
import ija.ija2020.project.warehouse.Vehicle;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Map;
import java.util.Scanner;
import java.util.stream.Collectors;

/***
 * Class that loads order from text representation in file and distributes order to warehouse
 * Author: Marián Zimmerman, xzimme03
 */
public class OrderPlanner {

    private ArrayList<Item> order = new java.util.ArrayList<Item>();
    private Warehouse warehouse;

    /***
     *
     * @param warehouse Warehouse to which will be OrderPlanner connected
     */
    public OrderPlanner(Warehouse warehouse) {
        this.warehouse = warehouse;
    }

    /***
     *
     * @param warehouse Warehouse to which will be OrderPlanner connected
     */
    public void setWarehouse(Warehouse warehouse) {
        this.warehouse = warehouse;
    }

    /***
     *
     * @param path Path to file containing text representation of order
     */
    public void loadOrder(String path){
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
                    order.add(item);
                }

            }

            myReader.close();
        }
        catch (FileNotFoundException e)  {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }

    }

    /***
     * Prints order
     */

    public void printOrder(){
        Map<String, Long> counting = this.order.stream().collect(
                Collectors.groupingBy(Item::getType, Collectors.counting()));
        System.out.println("Nacitana objednavka: " + counting);
    }

    /***
     * Distributes orders to vehicles
     */
    public void getItems(){
        Vehicle vehicle = this.warehouse.readyVehicle();
        if (vehicle == null){
            System.out.println("Ziadne vozidlo k dispozicii");
            return;
        }
        vehicle.getOrder(this.order);


    }



}
