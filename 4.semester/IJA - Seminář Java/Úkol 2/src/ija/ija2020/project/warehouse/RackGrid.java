package ija.ija2020.project.warehouse;

import ija.ija2020.project.grid.Grid;
import ija.ija2020.project.warehouse.*;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.util.stream.Collectors;

/***
 * Class representing one grid of rack
 * Author: Vanessa Jóriová, xjorio00
 */

public class RackGrid {
    private ArrayList<Item> items = new ArrayList<Item>();
    private int maxCapacity = 10;
    private int amount = 0;     //current amount of goods
    private Grid grid;

    /***
     *
     * @param grid Grid to which will RackGrid connect
     */
    public RackGrid(Grid grid) {
        this.grid = grid;
    }

    /***
     *
     * @param item Item to be added to rack
     */
    public void addItem(Item item){
        this.items.add(item);
        this.amount++;
    }

    /***
     *
     * @return True if full, False if not
     */

    public boolean isFull(){
        if (this.amount < this.maxCapacity){
            return false;
        }
        else {
            return true;
        }
    }

    /***
     *
     * @return All items stored in given RackGrid
     */

    public ArrayList<Item> getItems() {
        return items;
    }

    /***
     *
     * @param toRemove Item that will be removed if found
     * @return True if found, False if not
     */
    public boolean findAndRemove (Item toRemove){
        for (Item item: items){
            if (item.equals(toRemove)){
                items.remove(item);
                return true;
            }
        }
        return false;
    }

    /***
     * Computes stats of item in given rack-grid: types and amount of items of given type
     */

    public void getStats(){
        Map<String, Long> counting = items.stream().collect(
                Collectors.groupingBy(Item::getType, Collectors.counting()));
        System.out.println(counting);
    }

    /***
     *
     * @return Capacity of given rack-grid
     */
    public int getMaxCapacity() {
        return maxCapacity;
    }
}
