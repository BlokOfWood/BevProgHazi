class Team:
    def __init__(self, employeeName, project, role):
        self._employeeName = employeeName
        self._project = project
        self._role = role

        print("-- Developer létrehozva. --")

    def __str__(self):
        return f"{self._employeeName} a {self._project}-en dolgozik {self._role} szerepkörben."

    @property
    def employeeName(self):
        return self._employeeName

    @property
    def project(self):
        return self._project


if __name__ == '__main__':
    Ricsi = Team("Ricsi", "SolArch", "Frontend")
    print(Ricsi)

    Angéla = Team("Angéla", "ZerTeng", "Tesztelő")
    print(Angéla)

    Peti = Team("Peti", "KefERP", "Backen")
    print(Peti)

    Éva = Team("Éva", "KefERP", "Frontend")
    print(Éva)

    print()

    employeeList = [Ricsi, Angéla, Peti, Éva]

    for index1 in range(0, len(employeeList)):
        for index2 in range(index1 + 1, len(employeeList)):
            if employeeList[index1].project == employeeList[index2].project:
                print(f"{employeeList[index1].employeeName} és {employeeList[index2].employeeName} dolgozik egy projekten.")

