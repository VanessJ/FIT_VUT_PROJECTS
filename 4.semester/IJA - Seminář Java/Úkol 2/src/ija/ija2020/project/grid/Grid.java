package ija.ija2020.project.grid;

import ija.ija2020.project.warehouse.DeliveryPoint;
import ija.ija2020.project.warehouse.Rack;

/** Represents one grid of map with x and y coordinate
 * Author: Marián Zimmerman, xzimme03
 *
 *
 */

public class Grid {
    int x;
    int y;
    private Rack rack = null;
    private DeliveryPoint deliveryPoint = null;


    /***
     *
     * @return True if grid contains Rack, False if not
     */
    public boolean isRack() {
        if (this.rack == null) {
            return false;
        } else {
            return true;
        }
    }

    /***
     *
     * @return True if grid contains Delivery Point, False if not
     */
    public boolean isDP() {
        if (this.deliveryPoint == null) {
            return false;
        } else {
            return true;
        }
    }

    /**
     *
     * @param x sets x coordinate
     * @param y sets y coordinate
     */
    public void setCoord(int x, int y){
        this.x = x;
        this.y = y;
    }

    /***
     *
     * @param deliveryPoint binds grid with Delivery Point
     */
    public void setDeliveryPoint(DeliveryPoint deliveryPoint) {
        this.deliveryPoint = deliveryPoint;
    }

    /***
     *
     * @param rack bind grid with rack
     */
    public void setRack(Rack rack){
        this.rack = rack;
    }
}
