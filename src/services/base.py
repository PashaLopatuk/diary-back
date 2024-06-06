class BaseService[RepositoryType]:

    def __init__(self, repository: RepositoryType, **kwargs) -> None:
        self.repository: RepositoryType = repository
        self.kwargs: dict = kwargs
