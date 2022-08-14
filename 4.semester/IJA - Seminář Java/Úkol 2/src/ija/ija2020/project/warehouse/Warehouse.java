package ija.ija2020.project.warehouse;

import ija.ija2020.project.warehouse.*;
import ija.ija2020.project.grid.Map;

import java.util.ArrayList;

/***
 * Class that represents warehouse
 * Author: Vanessa Jóriová, xjorio00
 */

public class Warehouse {

    private DeliveryPoint delivery;
    private Map map;
    private ArrayList<Rack> racks = new ArrayList<Rack>();
    private ArrayList<Vehicle> vehicles = new ArrayList<Vehicle>();
    int capacity;
    int amount;

    /***
     *
     * @param delivery Delivery Point of warehouse
     */
    public void setDelivery(DeliveryPoint delivery) {
        this.delivery = delivery;
    }

    public void setRacks(ArrayList<Rack> racks) {
        int capacity = 0;
        this.racks = racks;
        for (Rack rack : racks){
            int rackCap = rack.getCapacity();
            capacity = rackCap + capacity;

        }
        this.capacity = capacity;
    }

    /***
     *
     * @return Vehicle that is not occupied with order
     */

    public Vehicle readyVehicle(){
        for (Vehicle vehicle : vehicles){
            if (vehicle.isReady()){
                return vehicle;
            }
        }
        return null;
    }

    /***
     * Finds and removes given item
     * @param item Needed item
     * @return Number of rack that contained needed item ( -1 if search unsuccessful)
     */

    public int findAndRemove(Item item){
        for (Rack rack : racks){
            int number = rack.findAndRemove(item);
            if (number > 0){
                return number;
            }

        }

        return -1;
    }

    /**
     *
     * @param item Item to be added
     * @return True if adding of item was successful, False if warehouse is full
     */
    public boolean addItem(Item item){
        for (Rack rack : racks){
            if (!rack.isFull()){
                rack.addItem(item);
                this.amount++;
                return true;
            }
        }
        System.out.println("Sklad je plny\n");
        return false;
    }

    /***
     *
     * @param vehicle Vehicle to be added
     */
    public void addVehicle(Vehicle vehicle){
        this.vehicles.add(vehicle);
    }

    /***
     * Gets stats of racks
     */
    public void getStats(){
        for (Rack rack : racks){
            rack.getStats();
        }
    }

    public int getAmount() {
        return amount;
    }

    /***
     *
     * @return True if warehouse is occupied to its full capacity, False if not
     */

    public boolean isFull(){
        if (this.amount < this.capacity){
            return false;
        }
        else {
            return true;
        }
    }

    /***
     *
     * @param map Internal representation that represents given warehouse
     */
    public void setMap(Map map) {
        this.map = map;
    }
}
