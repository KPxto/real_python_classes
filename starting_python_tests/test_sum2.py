def test_sum():
    assert sum([1, 2, 3]) == 6, "Should be 6"


# essa teste aqui vai levantar um assertion error
# a soma dos números da tupla deve dar 5 e não 6
# veja na mensagem de erro que ele informa onde foi a falha
# e qual foi a função q falhou
def test_sum_tuple():
    assert sum((1, 2, 2)) == 6, "Should be 6"


if __name__ == "__main__":
    test_sum()
    test_sum_tuple()
    print("Everything passed")