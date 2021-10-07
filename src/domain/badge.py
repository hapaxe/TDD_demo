class Badge:
    def __eq__(self, other):
        if isinstance(other, Badge):
            return True
