drop table "smuggler_guard_coworking";
drop table "smuggler_prison";
drop table "guard_prison";
drop table "guard_shift";
drop table "product_ingredients";
drop table "product_allergens";
drop table "ingredient";
drop table "product";
drop table "type";
drop table "allergen";
drop table "item";
drop table "order";
drop table "person";
drop table "shift";
drop table "prison";

create table "prison" (
    "id" INT GENERATED AS IDENTITY NOT NULL PRIMARY KEY ,
    "street" VARCHAR(255) NOT NULL,
    "city" VARCHAR(255) NOT NULL,
    "state" VARCHAR(255) NOT NULL
);

create table "shift" (
    "id" INT GENERATED AS IDENTITY NOT NULL,
    -- 1-7 --
    "day" INT NOT NULL
                     CHECK("day" BETWEEN 1 AND 7),
    -- format: 08.00
    "shift_start" NUMBER(4,2) NOT NULL
                      CHECK("shift_start" BETWEEN 00.00 AND 23.59),
    "shift_end" NUMBER(4,2) NOT NULL
                     CHECK("shift_end" BETWEEN 00.00 AND 23.59),
    "prison_id" INT NOT NULL,
    CONSTRAINT "shift_prison_id_fk"
                     FOREIGN KEY  ("prison_id") references "prison" ("id")
                     ON DELETE CASCADE,
    CONSTRAINT "shift_pk"
                     PRIMARY KEY("prison_id","id")

);

create table "person"(
    "id" INT GENERATED AS IDENTITY NOT NULL PRIMARY KEY,
    "name" VARCHAR(255) NOT NULL,
    "surname" VARCHAR(255) NOT NULL,
    "role" VARCHAR(255) NOT NULL
                    CHECK("role" IN ('PRISONER', 'SMUGGLER', 'GUARD')),
    "login" VARCHAR(255) DEFAULT NULL, ---prisoner/smuggler only
    "cell_type" VARCHAR(255) DEFAULT NULL, ---prisoner only
    "cell_number" INT DEFAULT NULL, ---prisoner only
    "in_prison" INT DEFAULT NULL, ---prisoner only
    "in_prison_start" TIMESTAMP DEFAULT NULL, ---prisoner only
    "in_prison_end" TIMESTAMP DEFAULT NULL, ---prisoner only
    CONSTRAINT "person_in_prison_fk"
                     FOREIGN KEY ("in_prison") REFERENCES "prison" ("id")
                     ON DELETE CASCADE

);

create table "order"(
    "id" INT GENERATED AS IDENTITY NOT NULL PRIMARY KEY,
    "delivery_day" TIMESTAMP NOT NULL,
    "state" VARCHAR(255) NOT NULL
                     CHECK("state" IN ('RECEIVED', 'CONFIRMED', 'DECLINED', 'IN_PROGRESS', 'ON_THE_WAY', 'DELIVERED')),
    "delivery_type" VARCHAR(255) NOT NULL,
    "price" NUMBER(10,2) NOT NULL,
    "made_by" INT NOT NULL,
    "delivered_by" INT NOT NULL,
    CONSTRAINT "order_mady_by_fk"
                     FOREIGN KEY ("made_by") REFERENCES "person" ("id")
                     ON DELETE CASCADE,
    CONSTRAINT "order_delivered_by_fk"
                    FOREIGN KEY ("delivered_by") REFERENCES "person" ("id")
                    ON DELETE SET NULL
);

create table "item"(
  "id" INT GENERATED AS IDENTITY NOT NULL PRIMARY KEY,
  --short description of item type - knife...
  "type" VARCHAR(255) NOT NULL
);

create table "allergen"(
    "id" INT GENERATED AS IDENTITY NOT NULL PRIMARY KEY,
    "name" VARCHAR(255) NOT NULL,
    "number" INT NOT NULL
                       CHECK("number" BETWEEN 1 AND 14)
);

create table "type"(
    "id" INT GENERATED AS IDENTITY NOT NULL PRIMARY KEY,
    --short description of product type - bread, pastry...
    "type_desc" VARCHAR(255) NOT NULL
);

create table "product"(
    "id" INT GENERATED AS IDENTITY NOT NULL PRIMARY KEY,
    "weight" NUMBER(15,4) NOT NULL,
    "price" NUMBER(15, 2) NOT NULL,
    "gluten" VARCHAR(255) DEFAULT 'GLUTEN'
                      CHECK ("gluten" IN ('GLUTEN', 'GLUTEN_FREE')),
    "type_id" INT NOT NULL,
    "item_id" INT NOT NULL,
    "order_id" INT NOT NULL,
    CONSTRAINT "product_type_fk"
                           FOREIGN KEY ("type_id") REFERENCES "type" ("id")
                           ON DELETE CASCADE,
    CONSTRAINT "product_item_fk"
                           FOREIGN KEY ("item_id") REFERENCES "item" ("id")
                           ON DELETE CASCADE,
    CONSTRAINT "product_order_fk"
                           FOREIGN KEY ("order_id") REFERENCES "order" ("id")
                           ON DELETE CASCADE
);


create table "ingredient" (
    "id" INT GENERATED AS IDENTITY NOT NULL PRIMARY KEY,
    "amount_in_stock" NUMBER (15,4) NOT NULL,
    "price" NUMBER(10,2) NOT NULL,
    "ordered_amount" NUMBER (15,4) NOT NULL
);
-- Entity relationships

--product made of ingredients
create table "product_ingredients"(
    "product_id" INT NOT NULL,
    "ingredient_id" INT NOT NULL,
    CONSTRAINT "product_ingredients_product_id_fk"
                           FOREIGN KEY ("product_id") REFERENCES "product" ("id")
                           ON DELETE CASCADE,
    CONSTRAINT "product_ingredients_ingredient_id_fk"
                           FOREIGN KEY ("ingredient_id") REFERENCES "ingredient" ("id")
                           ON DELETE CASCADE,
    CONSTRAINT "product_ingredients_pk"
                                  PRIMARY KEY("product_id", "ingredient_id")

);

create table "product_allergens"(
    "product_id" INT NOT NULL,
    "allergen_id" INT NOT NULL,
    CONSTRAINT "product_allergens_product_id_fk"
                           FOREIGN KEY ("product_id") REFERENCES "product" ("id")
                           ON DELETE CASCADE,
    CONSTRAINT "product_allergens_allergen_id_fk"
                           FOREIGN KEY ("allergen_id") REFERENCES "allergen" ("id")
                           ON DELETE CASCADE,
    CONSTRAINT "product_allergens_pk"
                                  PRIMARY KEY("product_id", "allergen_id")

);

--person guards on shift
create table "guard_shift" (
    "guard_id" INT NOT NULL,
    "shift_id" INT NOT NULL,
    "prison_id" INT NOT NULL,
    CONSTRAINT "guard_shift_shift_id_prison_id_fk"
                           FOREIGN KEY ("prison_id", "shift_id") REFERENCES "shift" ("prison_id","id")
                           ON DELETE CASCADE,
    CONSTRAINT "guard_shift_guard_id_fk"
                           FOREIGN KEY ("shift_id") REFERENCES "person" ("id")
                           ON DELETE CASCADE,
    CONSTRAINT "guard_shift_pk"
                           PRIMARY KEY ("guard_id", "shift_id", "prison_id")
);

--person works as guard in prison
create table "guard_prison" (
    "guard_id" INT NOT NULL,
    "prison_id" INT NOT NULL,
    CONSTRAINT "guard_prison_prison_id_fk"
                          FOREIGN KEY ("prison_id") REFERENCES "prison" ("id")
                          ON DELETE CASCADE,
    CONSTRAINT "guard_prison_guard_id_fk"
                          FOREIGN KEY ("guard_id") REFERENCES "person" ("id")
                          ON DELETE CASCADE,
    CONSTRAINT "guard_work_pk"
                          PRIMARY KEY ("guard_id", "prison_id")
);

--person works as smuggler in prison
create table "smuggler_prison" (
    "smuggler_id" INT NOT NULL,
    "prison_id" INT NOT NULL,
    CONSTRAINT "smuggler_prison_smuggler_id_fk"
                          FOREIGN KEY ("smuggler_id") REFERENCES "person" ("id")
                          ON DELETE CASCADE,
    CONSTRAINT "smuggler_prison_prison_id_fk"
                          FOREIGN KEY ("prison_id") REFERENCES "prison" ("id")
                          ON DELETE CASCADE,
    CONSTRAINT "smuggler_prison_pk"
                               PRIMARY KEY("smuggler_id", "prison_id")
);

--smuggler and guard coworking
create table "smuggler_guard_coworking" (
    "smuggler_id" INT NOT NULL,
    "guard_id" INT NOT NULL,
    CONSTRAINT "smuggler_guard_coworking_fk_smuggler"
                          FOREIGN KEY ("smuggler_id") REFERENCES "person" ("id")
                          ON DELETE CASCADE,
    CONSTRAINT  "smuggler_guard_coworking_fk_guard"
                          FOREIGN KEY ("guard_id") REFERENCES "person" ("id")
                          ON DELETE CASCADE,
    CONSTRAINT "smuggler_guard_coworking_pk"
                          PRIMARY KEY ("smuggler_id", "guard_id")


);

INSERT INTO "prison" ("street","city","state")
VALUES ('Bratislavska ulica', 'Bratislava', 'Slovensko');
INSERT INTO "prison" ("street","city","state")
VALUES ('Bozetechova', 'Brno', 'Cesko');


INSERT INTO "person" ("name","surname","role","login","cell_type","cell_number","in_prison","in_prison_start","in_prison_end")
VALUES ('John', 'Smith', 'PRISONER', 'xsmith00', 'regular', 77, 1, TO_DATE('1988-05-25', 'yyyy/mm/dd'), TO_DATE('2053-05-25', 'yyyy/mm/dd'));
INSERT INTO "person" ("name","surname","role","login","cell_type","cell_number","in_prison","in_prison_start","in_prison_end")
VALUES ('Eva', 'Hutson', 'PRISONER', 'xhutso02', 'solitary', 3, 2, TO_DATE('1995-06-06', 'yyyy/mm/dd'), TO_DATE('2023-06-06', 'yyyy/mm/dd'));

INSERT INTO "person" ("name","surname","role","login","cell_type","cell_number","in_prison","in_prison_start","in_prison_end")
VALUES ('Ben', 'Striker', 'SMUGGLER', 'xstrik04', NULL, NULL, NULL, NULL, NULL);
INSERT INTO "person" ("name","surname","role","login","cell_type","cell_number","in_prison","in_prison_start","in_prison_end")
VALUES ('Gustav', 'Husley', 'SMUGGLER', 'xhusle01', NULL, NULL, NULL, NULL, NULL);

INSERT INTO "person" ("name","surname","role","login","cell_type","cell_number","in_prison","in_prison_start","in_prison_end")
VALUES ('Antony', 'Montenegra', 'GUARD', NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "person" ("name","surname","role","login","cell_type","cell_number","in_prison","in_prison_start","in_prison_end")
VALUES ('Hugo', 'Targeryen', 'GUARD', NULL, NULL, NULL, NULL, NULL, NULL);


INSERT INTO "shift" ("day","shift_start","shift_end","prison_id")
VALUES (2, 14.00, 22.00, 1);
INSERT INTO "shift" ("day","shift_start","shift_end","prison_id")
VALUES (3, 22.00, 6.00, 1);
INSERT INTO "shift" ("day","shift_start","shift_end","prison_id")
VALUES (4, 14.00, 22.00, 2);
INSERT INTO "shift" ("day","shift_start","shift_end","prison_id")
VALUES (5, 6.00, 14.00, 2);

INSERT INTO "order" ("delivery_day","state","delivery_type","price","made_by","delivered_by")
VALUES (TO_DATE('2021-04-25', 'yyyy/mm/dd'), 'IN_PROGRESS', 'kitchen', 150.00, 1, 2);
INSERT INTO "order" ("delivery_day","state","delivery_type","price","made_by","delivered_by")
VALUES (TO_DATE('2021-05-30', 'yyyy/mm/dd'), 'RECEIVED', 'laundry room', 550.45, 2, 1);

INSERT INTO "item" ("type")
VALUES ('knife');
INSERT INTO "item" ("type")
VALUES ('screwdriver');

INSERT INTO "allergen" ("name","number")
VALUES ('milk',1);
INSERT INTO "allergen" ("name","number")
VALUES ('egg',2);

INSERT INTO "type" ("type_desc")
VALUES ('bread');
INSERT INTO "type" ("type_desc")
VALUES ('pastry');


INSERT INTO "product" ("weight","price","gluten","type_id","item_id","order_id")
VALUES (52, 5.5, 'GLUTEN', 2, 1, 1);
INSERT INTO "product" ("weight","price","gluten","type_id","item_id","order_id")
VALUES (158, 12.3, 'GLUTEN_FREE', 1, 2, 1);

INSERT INTO "ingredient" ("amount_in_stock","price","ordered_amount")
VALUES (507, 12.03, 40);
INSERT INTO "ingredient" ("amount_in_stock","price","ordered_amount")
VALUES (128, 56.25, 32);


INSERT INTO "product_ingredients" ("product_id","ingredient_id")
VALUES (1, 2);
INSERT INTO "product_ingredients" ("product_id","ingredient_id")
VALUES (1, 1);
INSERT INTO "product_ingredients" ("product_id","ingredient_id")
VALUES (2, 1);

INSERT INTO "product_allergens" ("product_id","allergen_id")
VALUES (1, 1);
INSERT INTO "product_allergens" ("product_id","allergen_id")
VALUES (2, 2);

INSERT INTO "guard_shift" ("guard_id","shift_id","prison_id")
VALUES (1, 2, 1);
INSERT INTO "guard_shift" ("guard_id","shift_id","prison_id")
VALUES (2, 3, 2);

INSERT INTO "guard_prison" ("guard_id","prison_id")
VALUES (1, 1);
INSERT INTO "guard_prison" ("guard_id","prison_id")
VALUES (2, 2);

INSERT INTO "smuggler_prison" ("smuggler_id","prison_id")
VALUES (2, 1);
INSERT INTO "smuggler_prison" ("smuggler_id","prison_id")
VALUES (1, 2);

INSERT INTO "smuggler_guard_coworking" ("smuggler_id","guard_id")
VALUES (2, 1);
INSERT INTO "smuggler_guard_coworking" ("smuggler_id","guard_id")
VALUES (1, 2);



