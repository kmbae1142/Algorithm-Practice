class Program {
    static void Main()
    {
        double 전공과목별_합 = 0;
        double 학점총합 = 0;

        for (int i = 0; i < 20; i++)
        {
            string[] input = Console.ReadLine().Split();
            string 과목명 = input[0];
            double 학점 = double.Parse(input[1]);
            string 등급 = input[2];

            if (등급 == "P") continue;

            switch (등급)
            {
                case "A+":
                    전공과목별_합 += 학점 * 4.5;
                    break;
                case "A0":
                    전공과목별_합 += 학점 * 4.0;
                    break;
                case "B+":
                    전공과목별_합 += 학점 * 3.5;
                    break;
                case "B0":
                    전공과목별_합 += 학점 * 3.0;
                    break;
                case "C+":
                    전공과목별_합 += 학점 * 2.5;
                    break;
                case "C0":
                    전공과목별_합 += 학점 * 2.0;
                    break;
                case "D+":
                    전공과목별_합 += 학점 * 1.5;
                    break;
                case "D0":
                    전공과목별_합 += 학점 * 1.0;
                    break;
                case "F":
                    전공과목별_합 += 학점 * 0.0;
                    break;
            }

            학점총합 += 학점;
            }

        Console.WriteLine("{0:F6}", 전공과목별_합 / 학점총합);
    }
}
