package ija.ija2020.homework1.store;

import ija.ija2020.homework1.goods.Goods;
import ija.ija2020.homework1.goods.GoodsItem;
import ija.ija2020.homework1.goods.GoodsShelf;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class StoreShelf implements GoodsShelf {

    private HashMap<Goods, List<GoodsItem>> shelfItems = new HashMap();

    @Override
    public void put(GoodsItem goodsItem) {
        Goods goods = goodsItem.goods();
        if (this.shelfItems.containsKey(goods)) {
            ((List)this.shelfItems.get(goods)).add(goodsItem);
        } else {
            ArrayList<GoodsItem> goodsArray = new ArrayList();
            goodsArray.add(goodsItem);
            this.shelfItems.put(goods, goodsArray);
        }
    }

    @Override
    public boolean containsGoods(Goods goods) {
        ArrayList<GoodsItem> goodsArray = (ArrayList<GoodsItem>) this.shelfItems.get(goods);
        if (goodsArray == null){
            return false;
        }
        else {
            if (goodsArray.isEmpty()){
                return false;
            }
            else {
                return true;
            }
        }
    }

    @Override
    public GoodsItem removeAny(Goods goods) {
        GoodsItem removed;
        ArrayList<GoodsItem> goodsArray = (ArrayList<GoodsItem>) this.shelfItems.get(goods);
        if (goodsArray == null) {
            return null;
        } else {
            if (goodsArray.isEmpty()){
                return null;
            }
            else {
                removed = goodsArray.remove(0);
                return removed;
            }
        }
    }

    @Override
    public int size(Goods goods) {
        ArrayList<GoodsItem> goodsArray = (ArrayList<GoodsItem>) this.shelfItems.get(goods);
        if (goodsArray == null){
            return 0;
        }
        else {
            return goodsArray.size();
        }
    }
}
