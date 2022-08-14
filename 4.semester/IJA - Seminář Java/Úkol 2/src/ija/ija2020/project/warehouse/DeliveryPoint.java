package ija.ija2020.project.warehouse;

import ija.ija2020.project.grid.Grid;

/***
 * Class representing DeliveryPoint
 * author Vanessa Jóriová, xjorio00
 */
public class DeliveryPoint {

    private Grid grid;

    /***
     *
     * @param grid Grid to which will be delivery point connected
     */

    public void setGrid(Grid grid) {
        this.grid = grid;
    }
}
