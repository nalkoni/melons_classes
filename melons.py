"""This file should have our order classes in it."""
class AbstractMelonOrder(object):
    """DOCSTRING"""

    def __init__(self, species, qty, order_type, shipped=False):
        """Initialize melon order attributes"""

        self.species = species
        self.qty = qty
        self.order_type = order_type


    def get_total(self):
        """Calculate price."""

        base_price = 5
        total = (1 + self.tax) * self.qty * base_price
        return total

    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic (in the US) melon order."""

    tax = 0.08

    def __init__(self, species, qty):
        """Initialize melon order attributes"""

        super(DomesticMelonOrder, self).__init__(species, qty, "domestic")


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    tax = 0.17

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes"""

        super(InternationalMelonOrder, self).__init__(species, qty, "international")
        
        self.country_code = country_code


    def get_country_code(self):
        """Return the country code."""

        return self.country_code
        """This file should have our order classes in it."""
        class AbstractMelonOrder(object):
            """DOCSTRING"""

            def __init__(self, species, qty, order_type, shipped=False):
                """Initialize melon order attributes"""

                self.species = species
                self.qty = qty
                self.order_type = order_type


            def get_total(self):
                """Calculate price."""

                base_price = 5
                total = (1 + self.tax) * self.qty * base_price
                return total

            def mark_shipped(self):
                """Set shipped to true."""

                self.shipped = True


        class DomesticMelonOrder(AbstractMelonOrder):
            """A domestic (in the US) melon order."""

            tax = 0.08

            def __init__(self, species, qty):
                """Initialize melon order attributes"""

                super(DomesticMelonOrder, self).__init__(species, qty, "domestic")


        class InternationalMelonOrder(AbstractMelonOrder):
            """An international (non-US) melon order."""

            tax = 0.17

            def __init__(self, species, qty, country_code):
                """Initialize melon order attributes"""

                super(InternationalMelonOrder, self).__init__(species, qty, "international")
                
                self.country_code = country_code


            def get_country_code(self):
                """Return the country code."""

                return self.country_code
