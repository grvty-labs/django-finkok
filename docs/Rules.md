XMLs Rules
==========

Please use the following format to build the XMLs to be used for the SAT. The
following list is case sensitive, so thread lightly to prevent errors. I used
a REGEX format to specify some types of the data expected by each variable.
In case you can't read the following list, please refer to the file
[Anexo20](https://github.com/letops/django-finkok/blob/master/docs/Anexo20RMF2014.doc?raw=true)

Although the rules are written in a json type object, you should remember that
it isn't a json object. This is because some objects can repeat themselves many
times in the same tree or branch.

```javascript
// ? means optional, if not marked as optional, then it is required.
// * means multiple, if marked with this symbol, than the object can repeat
//    itself multiple times.
// Remember, use the cfdi and tfd as objects, this means you should nest them
//   not use them as attributes.

Comprobante = {  
  certificado: '.*',  // Base64
  condicionesDePago: '.+',  // ?
  Descuento: '\d+\.\d{2}',  // ? // Or cfdi:t_Importe
  fecha: 'YYYY-MM-DDTHH:mm:ss',  //ISO-8601
  FechaFolioFiscalOrig: 'YYYY-MM-DDTHH:mm:ss',  // ? // ISO-8601
  folio: '[1-9]\d{0:19}',  // ?
  FolioFiscalOrig: '.+',  // ?
  formaDePago: '[Parcialidad 1 de N\.|.*]',
  LugarExpedicion: '.+',
  MetodoDePago: '[cheque|tarjeta de crédito o debito|depósito en cuenta|.+]',
  Moneda: '.*',  // ? // e.g. MXN, USD
  MontoFolioFiscalOrig: '\d+\.\d{2}',  // ? // Or cfdi:t_Importe
                                      // Use when formaDePago is Parcialidad
  MotivoDescuento: '.+', // ?
  noCertificado: '\d{20}'
  NumCtaPago: '.{4}.*',  // ?
  sello: '.*',  // Base64
  serie: '\w{1:25}'  // ?
  SerieFolioFiscalOrig: '.+',  // ?
  Subtotal:  '\d+\.\d{2}',  // Or cfdi:t_Importe
  TipoDeComprobante: '[ingreso|egreso|traslado]',  // What does this represent
                                                   // for the transmitter
  TipoCambio: '.*',  // ? // e.g. 1.00
  Total: '\d+\.\d{2}', // Subtotal - Descuentos + Trasladados - Retenidos
                      // Or cfdi:t_Importe

  /*
  Add this defaults
  xmlns:cfdi
  xmlns:xsi
  xsi:schemaLocation
  version='3.2'
  */

  'cfdi:Emisor': {
    rfc: '[a-zA-Z0-9]*',  // Or cfdi:t_RFC
    nombre: '.+',  // ?
    'cfdi:DomicilioFiscal': {  // ?  // Or cfdi:t_UbicacionFiscal
      calle: '.+',
      noExterior: '.*',  // ?
      noInterior: '.*',  // ?
      colonia: '.*',  // ?
      localidad: '.*',  // ?
      referencia: '.*',  // ?
      municipio: '.+',
      estado: '.+',
      pais: '.+',
      codigoPostal: '.+',
    },
    'cfdi:ExpedidoEn': {  // ?  // Or cfdi:t_Ubicacion
      calle: '.*',  // ?
      noExterior: '.*',  // ?
      noInterior: '.*',  // ?
      colonia: '.*',  // ?
      localidad: '.*',  // ?
      referencia: '.*',  // ?
      municipio: '.*',  // ?
      estado: '.*',  // ?
      pais: '.+',
      codigoPostal: '.*',  // ?
    },
    'cfdi:RegimenFiscal': {
      Regimen: '.+',
    },
  },

  'cfdi:Receptor': {
    rfc: '[a-zA-Z0-9]*',  // Or cfdi:t_RFC
    nombre: '.+',  // ?
    'cfdi:Domicilio': {  // ?  // Or cfdi:t_Ubicacion
      calle: '.*',  // ?
      noExterior: '.*',  // ?
      noInterior: '.*',  // ?
      colonia: '.*',  // ?
      localidad: '.*',  // ?
      referencia: '.*',  // ?
      municipio: '.*',  // ?
      estado: '.*',  // ?
      pais: '.+',
      codigoPostal: '.*',  // ?
    },
  },
  'cfdi:Conceptos': {
    'cfdi:Concepto': {
      cantidad: Decimal,
      unidad: '.+',
      noIdentificacion: '.+',  // ?
      descripcion: '.+',
      valorUnitario: '\d+\.\d{2}',  // Or cfdi:t_Importe
      importe: '\d+\.\d{2}',  // Or cfdi:t_Importe.
                              // cantidad * valorUnitario

      cfdi:InformacionAduanera
    },
    // 'cfdi:Concepto': {},
  },

  cfdi:Impuestos
    totalImpuestosTrasladados
    cfdi:Traslados
      cfdi:Traslado
          impuesto
          tasa
          importe

  cfdi:Complemento  // ?
    xmlns:cfdi
    tfd:TimbreFiscalDigital
      xmlns:tfd
      xmlns:xsi
      xsi:schemaLocation
      version
      UUID
      FechaTimbrado
      selloCFD
      noCertificadoSAT
      selloSAT

  cfdi:Addenda  // ?

};
```
