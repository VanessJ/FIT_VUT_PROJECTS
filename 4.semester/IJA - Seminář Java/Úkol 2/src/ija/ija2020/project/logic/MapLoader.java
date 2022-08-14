package ija.ija2020.project.logic;

import ija.ija2020.project.grid.Map;
import ija.ija2020.project.grid.Grid;
import ija.ija2020.project.warehouse.*;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;

/***
 * Class that loads map of warehouse and creates internal representation of given warehouse
 * Author: Marián Zimmerman, xzimme03
 */

public class MapLoader {


    private Map map = new Map();
    private Warehouse warehouse = new Warehouse();
    private DeliveryPoint dp = new DeliveryPoint();
    private ArrayList<Rack> racks = new ArrayList<Rack>();

    /***
     *
     * @param path Path to file containing data representation of Warehouse
     */
    public void loadMap(String path){


        try {
            File myObj = new File(path);
            Scanner myReader = new Scanner(myObj);
            while (myReader.hasNextLine()) {
                String data = myReader.nextLine();
                String[] split = data.split("\\s+");
                switch (split[0]){

                    case "Map":
                        this.parseMap(split[1]);
                        break;

                    case "DeliveryPoint":
                        this.parseDP(split[1]);
                        break;

                    case "Rack":
                        this.parseRack(split[1]);
                        break;

                    default:
                        System.out.println("Blbosť");
                }
            }
            this.buildWarehouse();
            myReader.close();

        }
        catch (FileNotFoundException e)  {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }

    }


    /***
     * Connects parts of warehouse together
     */
    private void buildWarehouse(){

        warehouse.setDelivery(this.dp);
        warehouse.setRacks(racks);
        warehouse.setMap(map);
        map.setWarehouse(warehouse);


    }

    /***
     *
     * @param toParse String containing map width and hight
     */
    private void parseMap(String toParse){
        String[] split = toParse.split("x");
        int x = Integer.parseInt(split[0]);
        int y = Integer.parseInt(split[1]);
        map.setLayout(x, y);
    }

    /***
     *
     * @return map - internal representation of warehouse
     */
    public Map getMap() {
        return map;
    }

    /***
     *
     * @param toParse String containing delivery point coordinates
     */

    private void parseDP(String toParse){
        String[] split = toParse.split(",");
        int x = Integer.parseInt(split[0]);
        int y = Integer.parseInt(split[1]);
        Grid grid = map.setAsDP(x, y, this.dp);
        this.dp.setGrid(grid);
    }

    /***
     *
     * @param toParse String containing coordinates of all grids ocuppied by rack
     */

    private void parseRack(String toParse){
        Rack rack = this.addRack();
        String[] split = toParse.split(":");
        for (String s :split){
            String[] split2 = s.split("_");

            for (String finalSplit :split2){
                String[] coords = finalSplit.split(",");
                int x = Integer.parseInt(coords[0]);
                int y = Integer.parseInt(coords[1]);
                Grid grid = map.setAsRack(x, y, rack);
                rack.addRackGrid(grid);

            }
        }
    }


    /***
     *
     * @return number of racks in warehouse
     */
    public int racksAmount(){
        int amount = this.racks.size();
        return amount;
    }

    /***
     *
     * @return added rack
     */
    public Rack addRack(){
        int order = this.racksAmount() + 1;
        Rack rack = new Rack(order);

        racks.add(rack);
        return rack;
    }
}



