from solution_parser import solutionParser
from answer_parser import answerParser
from corrector import Corrector

SOLUTION_XSLX_PATH = 'solution.xlsx'
ANSWER_CSV_PATH = 'GTA311-GTA-311_2024E — Quiz 01-réponses.csv'
QUESTION_COUNT = 10

if __name__ == '__main__':
    solution_parser = solutionParser()
    answer_parser = answerParser()
    corrector = Corrector()

    solution = solution_parser.parse_solution(SOLUTION_XSLX_PATH)

    answers = answer_parser.parse_answers(ANSWER_CSV_PATH)

    question = "Produisez une requête SQL qui permet d'identifier les pays qui comptent trois (3) fournisseurs ou plus de Northwind par ordre inverse de popularité incluant le nom du pays et le nombre de fournisseurs avec des libellés de colonnes en français dans le jeu de données produit."
    answer = "SELECT p.Nom_Pays AS Nom_Pays, COUNT(s.Id_Fournisseur) AS Nombre_Fournisseurs FROM Fournisseurs s JOIN Produits p ON s.Id_Fournisseur = p.Id_Fournisseur GROUP BY p.Nom_Pays HAVING COUNT(s.Id_Fournisseur) >= 3 ORDER BY Nombre_Fournisseurs DESC;"
    correction = "-- Section 1: grade between 0 and 0.5\n SELECT Country AS pays, COUNT(SupplierID) AS cat FROM `db-northwind`.Suppliers\n --Section 2: grade between 0 and 1\n GROUP BY Country HAVING COUNT(SupplierID) > 2 \n --section 3: grade between 0 and 0.5\n ORDER BY COUNT(SupplierID) DESC;"

    grade = corrector.correct(question, answer, correction)
    print(grade)



