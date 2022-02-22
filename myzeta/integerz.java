package myzeta;

public class integerz extends myzeta {
    public integerz() {
        super();
    }

    public Number generate(String size) {

        if (size.equalsIgnoreCase("large")) {
            // generates an integer between 2 and 100
            return 2 + (int) (Math.random() * ((100 - 98) + 1));
        } else if (size.equalsIgnoreCase("small")) {
            // generates an integer between 2 and 12
            return 2 + (int) (Math.random() * ((12 - 2) + 1));
        }

        return 0;
    }

    public static void main(String[] args) {
        integerz i = new integerz();
        for (int j = 0; j < 3; j++) {
            System.out.println("-------------------");
            System.out.println(i.generate("small"));
            System.out.println(i.generate("large"));
            System.out.println(i.generate(""));
            System.out.println("-------------------");
        }
    }
}
