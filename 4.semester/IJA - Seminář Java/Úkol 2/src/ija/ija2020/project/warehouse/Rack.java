package ija.ija2020.project.warehouse;
import ija.ija2020.project.warehouse.*;

import ija.ija2020.project.grid.Grid;

import java.util.ArrayList;
import java.util.Map;
import java.util.stream.Collectors;

/***
 * Class representing rack consisting of multiple map grids
 * Author: Vanessa Jóriová, xjorio00
 */

public class Rack {

    private ArrayList<RackGrid> grids = new ArrayList<RackGrid>();
    private int number;
    private int capacity;
    private int amount; //amount of goods on rack
    private int size;

    /***
     *
     * @param number Number of given rack
     */
    public Rack(int number) {
        this.number = number;
    }

    /***
     *
     * @param grid Grid to which rack will be connected
     */
    public void addRackGrid (Grid grid){
        RackGrid rackGrid = new RackGrid(grid);
        this.grids.add(rackGrid);
        this.setSize();
        this.setCapacity();
    }

    /***
     * Calculates capacity of given rack based of capacity of rack grids
     */

    private void setCapacity(){
        int capacity = 0;
        for (RackGrid grid: grids){
            int gridCapacity = grid.getMaxCapacity();
            capacity = capacity + gridCapacity;

        }

        this.capacity = capacity;
    }

    /***
     *
     * @param item Item which will be stored on rack
     */
    public void addItem(Item item){
        for (RackGrid grid : grids){
            if (!grid.isFull()){
                grid.addItem(item);
                this.amount++;
                break;
            }
        }
    }

    /***
     *
     * @param item One given item that will be removed from rack if found
     * @return number of rack which found the item
     */

    public int findAndRemove(Item item){
        for (RackGrid grid : grids){
            if(grid.findAndRemove(item)){
                return this.number;
            }
        }

        return -1;
    }

    /***
     *
     * @return Capacity of given rack
     */

    public int getCapacity() {
        return capacity;
    }

    /***
     *
     * @return True if full, False if not
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
     * Computes stats of items stored at given rack - all types and how many individual items
     * of given type does rack contain
     */

    public void getStats(){

        ArrayList<Item> whole = new ArrayList<Item>();
        for (RackGrid grid : grids){
            ArrayList<Item> temp = grid.getItems();
            whole.addAll(temp);
        }
        System.out.println("Regal cislo " + this.number + ": ");
        Map<String, Long> counting = whole.stream().collect(
                Collectors.groupingBy(Item::getType, Collectors.counting()));
        System.out.println(counting);
    }

    /***
     * Computes its size based on how many grids does rack occupy
     */
    private void setSize(){
        this.size = grids.size();
    }

    /***
     *
     * @return size of given rack
     */

    public int getSize() {
        return size;
    }
}
