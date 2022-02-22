package myzeta;

import java.lang.Math;

public abstract class myzeta {
    public myzeta() {

    }

    public static String operation() {
        float num = Math.random();
        if (num < (1 / 3)) {
            return "+";
        } else if (num < (2 / 3)) {
            return "-";
        } else {
            return "*";
        }
        // return "/"
    }

    public abstract Number generate(String size);
}