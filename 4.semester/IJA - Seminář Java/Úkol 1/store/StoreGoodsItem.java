package ija.ija2020.homework1.store;

import ija.ija2020.homework1.goods.Goods;
import ija.ija2020.homework1.goods.GoodsItem;

import java.time.LocalDate;

public class StoreGoodsItem implements GoodsItem {
    private Goods goods;
    private LocalDate date;

    public StoreGoodsItem(Goods goods, LocalDate date) {
        this.goods = goods;
        this.date = date;
    }

    @Override
    public Goods goods() {
        return this.goods;
    }

    @Override
    public boolean sell() {
        if (this.goods.remove(this) == true) {
            return true;
        }

        else {
            return false;
        }
    }
}
