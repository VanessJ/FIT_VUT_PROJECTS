package ija.ija2020.project;

import ija.ija2020.project.grid.Map;
import ija.ija2020.project.logic.MapLoader;
import ija.ija2020.project.logic.GoodsLoader;
import ija.ija2020.project.warehouse.Warehouse;
import ija.ija2020.project.logic.OrderPlanner;
import ija.ija2020.project.warehouse.Vehicle;

/***
 * Class demonstrating basic functionality of project in development
 * author: Vanessa Jóriová, xjorio00
 */
public class Main {

    public static void main(String[] args) {

    MapLoader mapLoader = new MapLoader();
    mapLoader.loadMap("data/map.txt");
    Map map = mapLoader.getMap();

    System.out.println("Demonstracia zakladnej funckionality projektu bez podpory GUI ");
    System.out.println("Autor: Vanessa Jóriová, xjorio00");
    System.out.println();

    System.out.println("Vizualizacia layoutu mapy po nacitani zo zdrojoveho subora");
    System.out.println("D - DeliveryPoint (výdajné miesto), R - Rack (Regál):\n");
    map.printMap();

    //loadne layout mapy a rozostaví regále atd.
    Warehouse warehouse = map.getWarehouse();

    //naplní regále tovarom
    GoodsLoader goodsLoader = new GoodsLoader();
    goodsLoader.loadGoods("data/goods.txt", warehouse);

    //vypíse aktuálny obsah regálov

    System.out.println();
    System.out.println("Vypis aktualneho obsadenia regálov: ");
    warehouse.getStats();

    //Nacíta objednávku a vybavi ju
    OrderPlanner orderPlanner = new OrderPlanner(warehouse);
    orderPlanner.loadOrder("data/order.txt");
    System.out.println();
    orderPlanner.printOrder();

    Vehicle vehicle = new Vehicle(10, warehouse);
    warehouse.addVehicle(vehicle);
    orderPlanner.getItems();

    System.out.println("\nStav po vybrati objednavky: ");
    warehouse.getStats();









    }
}