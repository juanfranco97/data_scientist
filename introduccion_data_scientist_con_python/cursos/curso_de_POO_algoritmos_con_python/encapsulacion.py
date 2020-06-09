class CasillaDeVotacion:
    def __init__(self, identificador, pais):
        self._identificador=identificador
        self._pais=pais
        self._region = None

    @property # getter
    def region(self):
        return self._region
    @region.setter
    def set_region(self, region):
        if region(self,region):
            self._region=region
        raise ValueError(f'la reguion {region} no es valida en {self._pais}')

casilla = CasillaDeVotacion(123, ['ciudad de Mexico','Morelos'])

casilla.region >>> Not # con este comando ejecutamos el getter que nos da informacion
# de self._region es una forma de acceder pero mas segura
casilla.region = 'Ciudad de mexico' # cuado se ejecuta este codigo entra el seter 
#y comprueba que la reguien este en paises de lo contrario no permitiria la asigancion ymandaria un arror
casilla.region >>> 'Ciudad de mexico'# aqui ya se comprobo la asiganacion y fue asignada
