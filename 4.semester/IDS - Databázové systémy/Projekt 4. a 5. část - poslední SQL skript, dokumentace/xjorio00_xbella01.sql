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
drop sequence "item_seq";
DROP MATERIALIZED VIEW "prisoner_order_count";


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
  "id" INT DEFAULT NULL PRIMARY KEY,
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


--Trigger 1: automaticka generacia hodnot primarneho kluca

CREATE SEQUENCE "item_seq"
    START WITH 1
    INCREMENT BY 1;
CREATE OR REPLACE TRIGGER item_pk_trigger
    BEFORE INSERT ON "item"
    FOR EACH ROW
BEGIN
    IF :NEW."id" IS NULL THEN
		:NEW."id" := "item_seq".NEXTVAL;
	END IF;
END;
/

--Trigger 2: zlozitejsia kontrola integrity - zadanie nespravnych dat pri specializacii danej osoby

CREATE OR REPLACE TRIGGER person_role_check
    BEFORE INSERT OR UPDATE ON "person"
    FOR EACH ROW
BEGIN
    IF :new."role" = 'PRISONER' THEN
        IF :new."cell_type" IS NULL THEN
            raise_application_error(-20000,'Prisoner role without cell type details');
        END IF;
        IF :new."cell_number" IS NULL THEN
            raise_application_error(-20001,'Prisoner role without cell number details');
        END IF;
        IF :new."in_prison_start" IS NULL THEN
            raise_application_error(-20002,'Prisoner role without arrival details');
        END IF;
        IF :new."in_prison_end" IS NULL THEN
            raise_application_error(-20003,'Prisoner role without release details');
        END IF;
        IF :new."login" IS NULL THEN
            raise_application_error(-20004,'Prisoner role without login');
        END IF;
    END IF;

    IF :new."role" = 'SMUGGLER' THEN
        IF :new."cell_type" IS NOT NULL THEN
            raise_application_error(-20005,'Smuggler role with invalid information (cell type)');
        END IF;
        IF :new."cell_number" IS NOT NULL THEN
            raise_application_error(-20006,'Smuggler role with invalid information (cell number)');
        END IF;
        IF :new."in_prison_start" IS NOT NULL THEN
            raise_application_error(-20007,'Smuggler role with invalid information (in_prison_start)');
        END IF;
        IF :new."in_prison_end" IS NOT NULL THEN
            raise_application_error(-20008,'Smuggler role with invalid information (in_prison_end)');
        END IF;
        IF :new."login" IS NULL THEN
            raise_application_error(-20009,'Smuggler role without login');
        END IF;
    END IF;
END;
/


--- Procedura 1: Pocita, kolko % vsetkych objednavok donasa SMUGGLER s ID v argumente (pokial ziadnu, vyvola sa vynimka)

CREATE OR REPLACE PROCEDURE smuggler_order_percentage (smuggler_id NUMBER) IS
    CURSOR "c_orders" IS SELECT "order"."delivered_by" FROM "order";
    order_num NUMBER;
    by_smuggler NUMBER;
    c_delivery  "order"."delivered_by"%TYPE;
BEGIN
        by_smuggler := 0;
    SELECT
        COUNT(*)
    INTO
        order_num
    FROM
        "order";

    OPEN "c_orders";
     LOOP
        FETCH "c_orders" INTO c_delivery;
        EXIT WHEN "c_orders"%notfound;
        IF
            c_delivery = smuggler_id
        THEN
            by_smuggler := by_smuggler + 1;
        END IF;
    END LOOP;
    CLOSE "c_orders";


    dbms_output.put_line(ROUND(by_smuggler / order_num * 100,2)
    || '% objednavok ma na starosti dany paserak, co je '
    || by_smuggler
    || ' z '
    || order_num);

EXCEPTION
    WHEN zero_divide THEN
        DBMS_OUTPUT.PUT_LINE('Dany paserak ma na starosti 0% objednavok');
END;
/


-- Procedura 2: Pocita, v kolkych objednavkach je dany item (pokial v ziadnych, vyvola sa vynimka)
CREATE OR REPLACE PROCEDURE how_many_items (item_type in VARCHAR) IS
    CURSOR "c_product" IS SELECT "product"."item_id" FROM "product";
    product_num NUMBER;
    item_id "product"."item_id"%TYPE;
    c_item  "product"."item_id"%TYPE;
BEGIN
    SELECT "id" INTO item_id
	FROM "item"
	WHERE "type" = item_type;

    product_num := 0;
    OPEN "c_product";
    LOOP
		FETCH "c_product" INTO c_item;

		EXIT WHEN "c_product"%NOTFOUND;

		IF c_item = item_id THEN
			product_num := product_num + 1;
		END IF;
	END LOOP;
	CLOSE "c_product";

    DBMS_OUTPUT.put_line(
			'Objekt ' || item_type || ' je pritomny v ' || product_num || ' vyrobkoch.'
		);

    EXCEPTION WHEN NO_DATA_FOUND THEN
	BEGIN
		DBMS_OUTPUT.put_line(
			'Objekt ' || item_type || ' nie je pritomny v ziadnom vyrobku'
		);
	END;
END;
/





--Inserty

INSERT INTO "prison" ("street","city","state")
VALUES ('Bratislavská ulica', 'Bratislava', 'Slovensko');
INSERT INTO "prison" ("street","city","state")
VALUES ('Božetechova', 'Brno', 'Česko');
INSERT INTO "prison" ("street","city","state")
VALUES ('Trieda Andreja Hlinku', 'Nitra', 'Slovensko');
INSERT INTO "prison" ("street","city","state")
VALUES ('Pražská ulica', 'Praha', 'Česko');

INSERT INTO "person" ("name","surname","role","login","cell_type","cell_number","in_prison","in_prison_start","in_prison_end")
VALUES ('John', 'Smith', 'PRISONER', 'xsmith00', 'regular', 77, 1, TO_DATE('1988-05-25', 'yyyy/mm/dd'), TO_DATE('2053-05-25', 'yyyy/mm/dd'));
INSERT INTO "person" ("name","surname","role","login","cell_type","cell_number","in_prison","in_prison_start","in_prison_end")
VALUES ('Eva', 'Hutson', 'PRISONER', 'xhutso02', 'solitary', 3, 2, TO_DATE('1995-06-06', 'yyyy/mm/dd'), TO_DATE('2023-06-06', 'yyyy/mm/dd'));
INSERT INTO "person" ("name","surname","role","login","cell_type","cell_number","in_prison","in_prison_start","in_prison_end")
VALUES ('Sirius', 'Black', 'PRISONER', 'xblack00', 'dementor-guarded', 10, 3, TO_DATE('1991-01-01', 'yyyy/mm/dd'), TO_DATE('2080-04-06', 'yyyy/mm/dd'));
INSERT INTO "person" ("name","surname","role","login","cell_type","cell_number","in_prison","in_prison_start","in_prison_end")
VALUES ('Andy', 'Varhol', 'PRISONER', 'xvarho05', 'regular', 55, 4, TO_DATE('1995-05-05', 'yyyy/mm/dd'), TO_DATE('2055-05-05', 'yyyy/mm/dd'));
INSERT INTO "person" ("name","surname","role","login","cell_type","cell_number","in_prison","in_prison_start","in_prison_end")
VALUES ('Don', 'Coloman', 'PRISONER', 'xcolom11', 'regular', 11, 3, TO_DATE('2020-04-03', 'yyyy/mm/dd'), TO_DATE('2032-04-03', 'yyyy/mm/dd'));

INSERT INTO "person" ("name","surname","role","login","cell_type","cell_number","in_prison","in_prison_start","in_prison_end")
VALUES ('Ben', 'Striker', 'SMUGGLER', 'xstrik04', NULL, NULL, NULL, NULL, NULL);
INSERT INTO "person" ("name","surname","role","login","cell_type","cell_number","in_prison","in_prison_start","in_prison_end")
VALUES ('Gustav', 'Husley', 'SMUGGLER', 'xhusle01', NULL, NULL, NULL, NULL, NULL);
INSERT INTO "person" ("name","surname","role","login","cell_type","cell_number","in_prison","in_prison_start","in_prison_end")
VALUES ('Hugh', 'Jackson', 'SMUGGLER', 'xjacks07', NULL, NULL, NULL, NULL, NULL);
INSERT INTO "person" ("name","surname","role","login","cell_type","cell_number","in_prison","in_prison_start","in_prison_end")
VALUES ('David', 'Backham', 'SMUGGLER', 'xbackh10', NULL, NULL, NULL, NULL, NULL);

INSERT INTO "person" ("name","surname","role","login","cell_type","cell_number","in_prison","in_prison_start","in_prison_end")
VALUES ('Antony', 'Montenegra', 'GUARD', NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "person" ("name","surname","role","login","cell_type","cell_number","in_prison","in_prison_start","in_prison_end")
VALUES ('Hugo', 'Targeryen', 'GUARD', NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "person" ("name","surname","role","login","cell_type","cell_number","in_prison","in_prison_start","in_prison_end")
VALUES ('Samuel', 'Stark', 'GUARD', NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "person" ("name","surname","role","login","cell_type","cell_number","in_prison","in_prison_start","in_prison_end")
VALUES ('Jack', 'Black', 'GUARD', NULL, NULL, NULL, NULL, NULL, NULL);


INSERT INTO "shift" ("day","shift_start","shift_end","prison_id")
VALUES (2, 14.00, 22.00, 1);
INSERT INTO "shift" ("day","shift_start","shift_end","prison_id")
VALUES (3, 22.00, 6.00, 1);
INSERT INTO "shift" ("day","shift_start","shift_end","prison_id")
VALUES (4, 14.00, 22.00, 2);
INSERT INTO "shift" ("day","shift_start","shift_end","prison_id")
VALUES (5, 6.00, 14.00, 2);
INSERT INTO "shift" ("day","shift_start","shift_end","prison_id")
VALUES (6, 10.00, 18.00, 3);
INSERT INTO "shift" ("day","shift_start","shift_end","prison_id")
VALUES (7, 18.00, 2.00, 3);
INSERT INTO "shift" ("day","shift_start","shift_end","prison_id")
VALUES (1, 8.00, 16.00, 4);
INSERT INTO "shift" ("day","shift_start","shift_end","prison_id")
VALUES (2, 00.00, 8.00, 4);


INSERT INTO "order" ("delivery_day","state","delivery_type","price","made_by","delivered_by")
VALUES (TO_DATE('2021-04-25', 'yyyy/mm/dd'), 'IN_PROGRESS', 'kitchen', 150.00, 1, 6);
INSERT INTO "order" ("delivery_day","state","delivery_type","price","made_by","delivered_by")
VALUES (TO_DATE('2021-05-30', 'yyyy/mm/dd'), 'RECEIVED', 'laundry room', 550.45, 2, 6);
INSERT INTO "order" ("delivery_day","state","delivery_type","price","made_by","delivered_by")
VALUES (TO_DATE('2021-07-28', 'yyyy/mm/dd'), 'IN_PROGRESS', 'laundry_room', 200.00, 1, 7);
INSERT INTO "order" ("delivery_day","state","delivery_type","price","made_by","delivered_by")
VALUES (TO_DATE('2021-06-06', 'yyyy/mm/dd'), 'CONFIRMED', 'library', 99.99, 3, 8);
INSERT INTO "order" ("delivery_day","state","delivery_type","price","made_by","delivered_by")
VALUES (TO_DATE('2021-04-30', 'yyyy/mm/dd'), 'ON_THE_WAY', 'showers', 68.70, 4, 8);
INSERT INTO "order" ("delivery_day","state","delivery_type","price","made_by","delivered_by")
VALUES (TO_DATE('2021-02-25', 'yyyy/mm/dd'), 'RECEIVED', 'showers', 44.50, 4, 8);

INSERT INTO "item" ("type")
VALUES ('knife');
INSERT INTO "item" ("type")
VALUES ('screwdriver');
INSERT INTO "item" ("type")
VALUES ('hammer');
INSERT INTO "item" ("type")
VALUES ('razor blade');
INSERT INTO "item" ("type")
VALUES ('axe');

INSERT INTO "allergen" ("name","number")
VALUES ('milk',1);
INSERT INTO "allergen" ("name","number")
VALUES ('egg',2);
INSERT INTO "allergen" ("name","number")
VALUES ('peanuts',3);
INSERT INTO "allergen" ("name","number")
VALUES ('wheat',4);
INSERT INTO "allergen" ("name","number")
VALUES ('soybeans',5);

INSERT INTO "type" ("type_desc")
VALUES ('bread');
INSERT INTO "type" ("type_desc")
VALUES ('pastry');
INSERT INTO "type" ("type_desc")
VALUES ('croissant');
INSERT INTO "type" ("type_desc")
VALUES ('pie');
INSERT INTO "type" ("type_desc")
VALUES ('bio_vegan_raw_lactose_free_baguette');


INSERT INTO "product" ("weight","price","gluten","type_id","item_id","order_id")
VALUES (52, 5.5, 'GLUTEN', 2, 1, 1);
INSERT INTO "product" ("weight","price","gluten","type_id","item_id","order_id")
VALUES (158, 12.3, 'GLUTEN_FREE', 1, 2, 1);
INSERT INTO "product" ("weight","price","gluten","type_id","item_id","order_id")
VALUES (300, 20.50, 'GLUTEN_FREE', 3, 3, 3);
INSERT INTO "product" ("weight","price","gluten","type_id","item_id","order_id")
VALUES (500, 51.30, 'GLUTEN_FREE', 5, 5, 4);
INSERT INTO "product" ("weight","price","gluten","type_id","item_id","order_id")
VALUES (350, 8.43, 'GLUTEN_FREE', 4, 4, 5);


INSERT INTO "ingredient" ("amount_in_stock","price","ordered_amount")
VALUES (507, 12.03, 40);
INSERT INTO "ingredient" ("amount_in_stock","price","ordered_amount")
VALUES (128, 56.25, 32);
INSERT INTO "ingredient" ("amount_in_stock","price","ordered_amount")
VALUES (32, 25.15, 12);
INSERT INTO "ingredient" ("amount_in_stock","price","ordered_amount")
VALUES (45, 36.68, 5);


INSERT INTO "product_ingredients" ("product_id","ingredient_id")
VALUES (1, 2);
INSERT INTO "product_ingredients" ("product_id","ingredient_id")
VALUES (1, 1);
INSERT INTO "product_ingredients" ("product_id","ingredient_id")
VALUES (2, 1);
INSERT INTO "product_ingredients" ("product_id","ingredient_id")
VALUES (3, 4);
INSERT INTO "product_ingredients" ("product_id","ingredient_id")
VALUES (5, 3);

INSERT INTO "product_allergens" ("product_id","allergen_id")
VALUES (1, 1);
INSERT INTO "product_allergens" ("product_id","allergen_id")
VALUES (2, 2);
INSERT INTO "product_allergens" ("product_id","allergen_id")
VALUES (3, 5);
INSERT INTO "product_allergens" ("product_id","allergen_id")
VALUES (5, 4);

INSERT INTO "guard_shift" ("guard_id","shift_id","prison_id")
VALUES (1, 2, 1);
INSERT INTO "guard_shift" ("guard_id","shift_id","prison_id")
VALUES (2, 3, 2);
INSERT INTO "guard_shift" ("guard_id","shift_id","prison_id")
VALUES (3, 5, 3);
INSERT INTO "guard_shift" ("guard_id","shift_id","prison_id")
VALUES (4, 8, 4);

INSERT INTO "guard_prison" ("guard_id","prison_id")
VALUES (1, 1);
INSERT INTO "guard_prison" ("guard_id","prison_id")
VALUES (2, 2);
INSERT INTO "guard_prison" ("guard_id","prison_id")
VALUES (3, 3);
INSERT INTO "guard_prison" ("guard_id","prison_id")
VALUES (4, 4);

INSERT INTO "smuggler_prison" ("smuggler_id","prison_id")
VALUES (2, 1);
INSERT INTO "smuggler_prison" ("smuggler_id","prison_id")
VALUES (1, 2);
INSERT INTO "smuggler_prison" ("smuggler_id","prison_id")
VALUES (4, 3);
INSERT INTO "smuggler_prison" ("smuggler_id","prison_id")
VALUES (3, 4);

INSERT INTO "smuggler_guard_coworking" ("smuggler_id","guard_id")
VALUES (2, 1);
INSERT INTO "smuggler_guard_coworking" ("smuggler_id","guard_id")
VALUES (1, 2);
INSERT INTO "smuggler_guard_coworking" ("smuggler_id","guard_id")
VALUES (4, 3);
INSERT INTO "smuggler_guard_coworking" ("smuggler_id","guard_id")
VALUES (3, 4);

-- Explain plans

--- Ktory uzivatel vytvoril aspon jednu objednavku a kolko ich vytvoril?

EXPLAIN PLAN  FOR
SELECT
        "p"."name" AS name,
        "p"."surname" AS surname,
        "p"."login" AS login,
        COUNT("o"."made_by") AS amount
FROM "order" "o"
JOIN "person" "p" ON "p"."id" = "o"."made_by"
WHERE "p"."cell_type" = 'regular'
GROUP BY "p"."id", "p"."name", "p"."surname", "p"."login"
HAVING COUNT("o"."id") > 0
ORDER BY amount DESC;

SELECT * FROM TABLE(DBMS_XPLAN.display);


--index

CREATE INDEX "person_cell_type_index" ON "person" ("cell_type");

--druhy EXPLAIN PLAN
EXPLAIN PLAN  FOR
SELECT
        "p"."name" AS name,
        "p"."surname" AS surname,
        "p"."login" AS login,
        COUNT("o"."made_by") AS amount
FROM "order" "o"
JOIN "person" "p" ON "p"."id" = "o"."made_by"
WHERE "p"."cell_type" = 'regular'
GROUP BY "p"."id", "p"."name", "p"."surname", "p"."login"
HAVING COUNT("o"."id") > 0
ORDER BY amount DESC;

SELECT * FROM TABLE(DBMS_XPLAN.display);



--Demonstratracie (cast 4)

--Trigger 1: automaticka generacia PK - vsetky itemy maju PK cez trigger
SELECT *  FROM "item";
-- aj novy predmet bude mat spravny PK
INSERT INTO "item" ("type")
VALUES ('sword');
SELECT *  FROM "item";


--Volania procedur
CALL smuggler_order_percentage(6);
CALL how_many_items('knife');

--Udelovanie prav
GRANT ALL ON "smuggler_prison" TO xbella01;
GRANT ALL ON "guard_prison" TO xbella01;
GRANT ALL ON "guard_shift" TO xbella01;
GRANT ALL ON "product_ingredients" TO xbella01;
GRANT ALL ON "product_allergens" TO xbella01;
GRANT ALL ON "ingredient" TO xbella01;
GRANT ALL ON "product" TO xbella01;
GRANT ALL ON "type" TO xbella01;
GRANT ALL ON "allergen" TO xbella01;
GRANT ALL ON "item" TO xbella01;
GRANT ALL ON "order" TO xbella01;
GRANT ALL ON "person" TO xbella01;
GRANT ALL ON "shift" TO xbella01;
GRANT ALL ON "prison" TO xbella01;


--Materialized View
CREATE MATERIALIZED VIEW "prisoner_order_count" AS
SELECT
	"p"."id",
	"p"."name",
	"p"."surname",
    "p"."login",
    "p"."role",
	COUNT("o"."made_by") AS "orders_count"
FROM "person" "p"
LEFT JOIN "order" "o"  ON "p"."id" = "o"."made_by"
WHERE  "p"."role" = 'PRISONER'
GROUP BY "p"."id","p"."name", "p"."surname","p"."login","p"."role";


GRANT ALL ON "prisoner_order_count" TO xbella01;

-- vypis Materialized View
SELECT * FROM "prisoner_order_count";

-- uprava tabuliek
UPDATE "person" SET "name" = 'updatename' WHERE "id" = 1;

--vypis zmenenej tabulky
SELECT * FROM "person" "p"
WHERE "p"."role" = 'PRISONER';

--Materialized View sa nezmenil
SELECT * FROM "prisoner_order_count";


--- Trigger 2: nemoznost pridania neuplnych udajov pri generalizacii/specializacii

-- chybajuci cell type (popr. ine nutne udaje) vedu na chybu
INSERT INTO "person" ("name","surname","role","login", "cell_number","in_prison","in_prison_start","in_prison_end")
VALUES ('Macko', 'Pusik', 'PRISONER', 'xsmith00', 77, 1, TO_DATE('1988-05-25', 'yyyy/mm/dd'), TO_DATE('2053-05-25', 'yyyy/mm/dd'));

-- na chybu rovnako vedu aj nadmerne udaje (pokus o vlozenie smugglera s udajmi vazna)
INSERT INTO "person" ("name","surname","role","login","cell_type","cell_number","in_prison","in_prison_start","in_prison_end")
VALUES ('Ujo', 'Smuggler', 'SMUGGLER', 'xujo00', 'regular', 11, 3, TO_DATE('2020-04-03', 'yyyy/mm/dd'), TO_DATE('2032-04-03', 'yyyy/mm/dd'));








