package ija.ija2020.project.warehouse;

import java.util.Objects;

/***
 * Class representing one item in racks
 * Author: Vanessa Jóriová
 */

public class Item {

    private String type;

    /***
     *
     * @param type Type of goods
     */
    public Item(String type) {
        this.type = type;
        //System.out.println("Item pridany");
    }

    /***
     *
     * @return Type of given item
     */
    public String getType() {
        return type;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Item item = (Item) o;
        return Objects.equals(type, item.type);
    }

    @Override
    public int hashCode() {
        return Objects.hash(type);
    }
}


