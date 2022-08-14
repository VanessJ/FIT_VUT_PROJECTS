package ija.ija2020.homework1.store;

import ija.ija2020.homework1.goods.Goods;
import ija.ija2020.homework1.goods.GoodsItem;

import java.time.LocalDate;
import java.util.Objects;
import java.util.ArrayList;

public class StoreGoods implements Goods {
    private String name;
    private ArrayList<GoodsItem> items = new ArrayList<GoodsItem>();

    public StoreGoods(String name) {
        this.name = name;
    }

    @Override
    public String getName() {

        return this.name;
    }

    @Override
    public boolean addItem(GoodsItem goodsItem) {
            items.add(goodsItem);
            return true;
    }

    @Override
    public GoodsItem newItem(LocalDate localDate) {
        GoodsItem goodsItem = new StoreGoodsItem(this, localDate);
        this.addItem(goodsItem);

        return goodsItem;
    }

    @Override
    public boolean remove(GoodsItem goodsItem) {
        int index;
        index = items.indexOf(goodsItem);
        if (index == -1){
            return false;
        }
        else {

            items.remove(index);
        }

        return true;
    }

    @Override
    public boolean empty() {

        return items.isEmpty();
    }

    @Override
    public int size() {
        return items.size();
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        StoreGoods that = (StoreGoods) o;
        return Objects.equals(name, that.name);
    }

    @Override
    public int hashCode() {
        return Objects.hash(name);
    }
}
