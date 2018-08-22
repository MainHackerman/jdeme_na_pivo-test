import unittest
import sys
import io

oldstdin, sys.stdin = sys.stdin, io.StringIO('10\n1000\nPepa\n5')

try:
  import project
finally:
  sys.stdin = oldstdin


class TestStaticVariables(unittest.TestCase):
    def test_pivo(self):
        self.assertEqual(project.pivo, 80)


class TestInputedVariables(unittest.TestCase):

    def test_poce_lidi(self):
        self.assertEqual(project.pocet_lidi, 10)

    def test_rozpocet_osoba(self):
        self.assertEqual(project.rozpocet_osoba, 1000)

    def test_zastupce(self):
        self.assertEqual(project.zastupce, 'Pepa')

    def test_studenti(self):
        self.assertEqual(project.studeti, 5)


class TestComputedVariables(unittest.TestCase):
    def test_student_price(self):
        self.assertEqual(project.stud_pivo, project.pivo * 0.65)

    def test_rozpocet_vsichni(self):
        self.assertEqual(project.rozpocet_vsichni, project.pocet_lidi * project.rozpocet_osoba)

    def test_rozcpocet_studenti(self):
        self.assertEqual(project.rozpocet_studenti, project.stud_pivo * project.studeti)

    def test_rozpocet_ostatni(self):
        self.assertEqual(project.rozpocet_ostatni, project.rozpocet_vsichni - project.rozpocet_studenti)

    def test_piva_studenti(self):
        self.assertEqual(project.rozpocet_studenti, project.rozpocet_studenti // project.stud_pivo)

    def test_piva_ostatni(self):
        self.assertEqual(project.piva_ostatni, project.piva_ostatni // project.pivo)

    def test_cena_studenti(self):
        self.assertEqual(project.cena_studenti, project.piva_studenti * project.stud_pivo)

    def test_cena_ostatni(self):
        self.assertEqual(project.cena_ostatni, project.piva_ostatni * project.pivo)

if __name__ == '__main__':
    unittest.main()