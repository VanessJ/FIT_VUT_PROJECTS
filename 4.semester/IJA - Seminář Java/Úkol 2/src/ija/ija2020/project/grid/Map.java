package ija.ija2020.project.grid;
import ija.ija2020.project.grid.Grid;
import ija.ija2020.project.warehouse.DeliveryPoint;
import ija.ija2020.project.warehouse.Rack;
import ija.ija2020.project.warehouse.Warehouse;

public class Map {
    /***
     * Internal representation of warehouse consisting of multiple grids
     * Author: Marián Zimmerman, xzimme03
     */

    private Warehouse warehouse;
    private Grid [][] layout;

    /***
     *
     * @param x width of map
     * @param y height of map
     */
    public void setLayout (int x, int y){
        layout = new Grid [x][y];
        for (int i = 0; i < layout.length; i++) {
            for (int j = 0; j < layout[i].length; j++) {
                layout[i][j] = new Grid();
            }
        }
    }

    /***
     *
     * @return warehouse to which given map belongs
     */

    public Warehouse getWarehouse() {
        return warehouse;
    }

    /***
     *
     * @param x grid x coordinate
     * @param y grid y coordinate
     * @param dp delivery point that will be binded to given grid
     * @return grid set as delivery point
     */

    public Grid setAsDP(int x, int y, DeliveryPoint dp){
        Grid grid = layout[x][y];
        grid.setCoord(x, y);
        grid.setDeliveryPoint(dp);
        return grid;
    }

    /***
     *
     * @param x grid x coordinate
     * @param y grid y coordinate
     * @param rack rack that will be binded to given grid
     * @return grid set as part of rack
     */

    public Grid setAsRack(int x, int y, Rack rack){
        Grid grid = layout[x][y];
        grid.setCoord(x, y);
        grid.setRack(rack);
        return grid;

    }

    /***
     * Prints console representation of map
     */

    public void printMap(){

        for (Grid [] grid_row : this.layout)
        {
            for (Grid grid : grid_row)
            {
                if (grid.isRack()){
                    System.out.print(" R ");
                }
                else if (grid.isDP()){
                    System.out.print(" D ");
                }

                else {
                    System.out.print(" * ");
                }

                //System.out.print(y + " ");
            }
            System.out.println();
        }
    }

    /***
     *
     * @param warehouse Warehouse to which map will be connected
     */

    public void setWarehouse(Warehouse warehouse) {
        this.warehouse = warehouse;
    }
}
