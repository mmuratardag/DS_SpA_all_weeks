
CREATE TABLE singer (
    id SERIAL NOT NULL,
    name VARCHAR (100),
);

INSERT INTO "public"."singer"("id", "name") VALUES(1, 'Nicki Minaj') RETURNING "id", "name";
INSERT INTO "public"."singer"("id", "name") VALUES(2, 'Lady Gaga') RETURNING "id", "name";
INSERT INTO "public"."singer"("id", "name") VALUES(3, 'Taylor Swift') RETURNING "id", "name";
INSERT INTO "public"."singer"("id", "name") VALUES(4, 'Tom Jones') RETURNING "id", "name";

CREATE TABLE song (
   id    INTEGER  PRIMARY KEY,
   name  CHARACTER VARYING(20),
   singer_id INTEGER,
   FOREIGN KEY(singer_id)
      REFERENCES singer(id) ON DELETE CASCADE
   );

INSERT INTO "public"."song"("id", "name", "singer_id") VALUES(1, 'Anaconda', 1) RETURNING "id", "name", "singer_id";
INSERT INTO "public"."song"("id", "name", "singer_id") VALUES(2, 'Paparazzi', 2) RETURNING "id", "name", "singer_id";
INSERT INTO "public"."song"("id", "name", "singer_id") VALUES(3, 'Bad Romance', 2) RETURNING "id", "name", "singer_id";
INSERT INTO "public"."song"("id", "name", "singer_id") VALUES(4, 'Sex Bomb', 4) RETURNING "id", "name", "singer_id";