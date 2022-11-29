tax_per_year = int(input())
basketball_shoes = tax_per_year - (0.40 * tax_per_year)
basketball_kit = basketball_shoes - (0.20 * basketball_shoes)
basketball_ball = basketball_kit / 4
basketball_accessories = basketball_ball / 5

jessy_expenses = tax_per_year + basketball_shoes + basketball_kit + basketball_ball + basketball_accessories

print(jessy_expenses)
