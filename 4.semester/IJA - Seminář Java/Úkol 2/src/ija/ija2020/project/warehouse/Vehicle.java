package ija.ija2020.project.warehouse;

import java.util.ArrayList;

/***
 * Class representing vehicle in warehouse
 * Author: Vanessa Jóriová, xjorio00
 */

public class Vehicle {

    int capacity;
    boolean ready = true;
    Warehouse warehouse;
    private ArrayList<Item> ordered = new ArrayList<Item>();
    private ArrayList<Item> held = new ArrayList<Item>();

    /***
     *
     * @param capacity Capacity of vehicle
     * @param warehouse Warehouse to which vehicle belongs
     */

    public Vehicle(int capacity, Warehouse warehouse) {
        this.capacity = capacity;
        this.warehouse = warehouse;
    }

    /***
     *
     * @param warehouse Warehouse to which vehicle belongs
     */

    public void setWarehouse(Warehouse warehouse) {
        this.warehouse = warehouse;
    }


    /***
     *
     * @return True if not ocuppied, False if occupied
     */
    public boolean isReady(){
        if (this.ready == true){
            return true;
        }
        else {
            return false;
        }
    }

    /***
     * Placeholder function that gets order without any coordination or pathfinding - subject to change
     * @param order List of items in order
     */

    //placeholder
    public void getOrder(ArrayList<Item> order ){
        ArrayList<Integer> racks = new ArrayList<Integer>();
        for (Item item : order){
            int rack = this.warehouse.findAndRemove(item);
            if (rack > 0){
                racks.add(rack);
            }
            else {
                System.out.println("V sklade sa nedala najsť objednavka pre " + item.getType());
            }
        }
        this.pathPrinter(racks);

    }

    public void pathPrinter(ArrayList<Integer> path){
        System.out.println();
        System.out.print("Vozik objednavku nasiel v regaloch: ");
        for (int rack : path){
            System.out.print(rack + ", ");
        }
        System.out.println();

    }



}


