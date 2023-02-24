"""
    Regionalatlas-API

    API zum [Regionalatlas Deutschland](https://regionalatlas.statistikportal.de/#) der statistischen Ämter des Bundes und der Länder.   Der Regionalatlas Deutschland der Statistischen Ämter des Bundes und der Länder visualisiert aktuell laut [statistischem Bundesamt](https://www.destatis.de/DE/Service/Statistik-Visualisiert/_inhalt.html) mehr als 160 Indikatoren aus 20 Themenbereichen für Bundesländer, Regierungsbezirke, Kreisfreie Städte und Landkreise. Grundlage des Regionalatlas ist die Regionaldatenbank Deutschland.    # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: kontakt@bund.dev
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from deutschland.Regionalatlas.api_client import ApiClient
from deutschland.Regionalatlas.api_client import Endpoint as _Endpoint
from deutschland.Regionalatlas.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types,
)


class DefaultApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.query_endpoint = _Endpoint(
            settings={
                "response_type": (
                    {
                        str: (
                            bool,
                            date,
                            datetime,
                            dict,
                            float,
                            int,
                            list,
                            str,
                            none_type,
                        )
                    },
                ),
                "auth": [],
                "endpoint_path": "/query",
                "operation_id": "query",
                "http_method": "GET",
                "servers": None,
            },
            params_map={
                "all": [
                    "layer",
                    "f",
                    "return_geometry",
                    "spatial_rel",
                    "where",
                    "out_fields",
                ],
                "required": [
                    "layer",
                    "f",
                    "return_geometry",
                    "spatial_rel",
                    "where",
                ],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "layer": (str,),
                    "f": (str,),
                    "return_geometry": (bool,),
                    "spatial_rel": (str,),
                    "where": (str,),
                    "out_fields": (str,),
                },
                "attribute_map": {
                    "layer": "layer",
                    "f": "f",
                    "return_geometry": "returnGeometry",
                    "spatial_rel": "spatialRel",
                    "where": "where",
                    "out_fields": "outFields",
                },
                "location_map": {
                    "layer": "query",
                    "f": "query",
                    "return_geometry": "query",
                    "spatial_rel": "query",
                    "where": "query",
                    "out_fields": "query",
                },
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

    def query(
        self,
        f,
        return_geometry,
        spatial_rel,
        where,
        layer="%7B%22source%22%3A%7B%22dataSource%22%3A%7B%22geometryType%22%3A%22esriGeometryPolygon%22%2C%22workspaceId%22%3A%22gdb%22%2C%22query%22%3A%22SELECT%20*%20FROM%20verwaltungsgrenzen_gesamt%20LEFT%20OUTER%20JOIN%20ai002_1_5%20ON%20ags%20%3D%20ags2%20and%20jahr%20%3D%20jahr2%20WHERE%20typ%20%3D%201%20AND%20jahr%20%3D%202020%20AND%20(jahr2%20%3D%202020%20OR%20jahr2%20IS%20NULL)%22%2C%22oidFields%22%3A%22id%22%2C%22spatialReference%22%3A%7B%22wkid%22%3A25832%7D%2C%22type%22%3A%22queryTable%22%7D%2C%22type%22%3A%22dataLayer%22%7D%7D",
        **kwargs
    ):
        """query  # noqa: E501

        Die gewünschten Daten lassen sich über GET-Parameter im Query-String spezifizieren.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.query(f, return_geometry, spatial_rel, where, layer="%7B%22source%22%3A%7B%22dataSource%22%3A%7B%22geometryType%22%3A%22esriGeometryPolygon%22%2C%22workspaceId%22%3A%22gdb%22%2C%22query%22%3A%22SELECT%20*%20FROM%20verwaltungsgrenzen_gesamt%20LEFT%20OUTER%20JOIN%20ai002_1_5%20ON%20ags%20%3D%20ags2%20and%20jahr%20%3D%20jahr2%20WHERE%20typ%20%3D%201%20AND%20jahr%20%3D%202020%20AND%20(jahr2%20%3D%202020%20OR%20jahr2%20IS%20NULL)%22%2C%22oidFields%22%3A%22id%22%2C%22spatialReference%22%3A%7B%22wkid%22%3A25832%7D%2C%22type%22%3A%22queryTable%22%7D%2C%22type%22%3A%22dataLayer%22%7D%7D", async_req=True)
        >>> result = thread.get()

        Args:
            f (str): Output-Format (z.B. 'json' oder 'html').
            return_geometry (bool): Boolsche Angabe, ob Angaben zur Geometrie gesendet werden sollen (z.B. 'false').
            spatial_rel (str): spational relation (z.B. 'esriSpatialRelIntersects').
            where (str): Spezifikation einer gewünschten Teilmenge der Daten (z.B.'1=1'' für alle Daten oder 'ags2 = 'DG' and jahr2 =  2020').
            layer (str): Komplexer Parameter, der im JSON-Format Details der Anfrage spezifiziert. In der Regel stellt enthält der layer-Parameter ein Objekt (in geschweiften Klammern), das seinerseits ein Objekt namens 'source' enthält. Das source-Objekt wiederum enthält ein Objekt, das zum einen das Objekt 'dataSource' und zum anderen ein Datum namens 'type' mit dem Wert 'dataLayer' enthält. In dataSource wird die gewünschte Tabelle spezifiziert (z.B. für Angaben zur Bevölkerungsdichte 'ai002_1_5') - im Folgenden mit dem Platzhalter *tableName* gekennzeichnet.  dataSource kann unterschiedlich aufgebaut sein und enthält entweder (a) Daten namens 'dataSourceName' (mit einem Wert wie z.B. 'regionalatlas.*tableName*'), 'workspaceId' (z.B.  'gdb') und 'type' (z.B. 'table') oder (b) Daten namens 'geometryType' (z.B. 'esriGeometryPolygon'), 'workspaceId' (z.B. 'gdb'), 'query' (mit einem SQL-Query, z.B. 'SELECT * FROM verwaltungsgrenzen_gesamt LEFT OUTER JOIN *tableName* ON ags = ags2 and jahr = jahr2 WHERE typ = 3 AND jahr = 2020 AND (jahr2 = 2020 OR jahr2 IS NULL)'), 'oidFields' (z.B. 'id'), 'spatialReference' (mit einem Objekt, das wiederum das Datum 'wkid' mit einem Wert wie 25832 umfasst), und 'type':'queryTable'.    Der SQL-Query dürfte für Nutzer*innen des Regionalatlas Deutschland weitgehend selbsterklärend sein, wobei man wissen muss dass die Variable *typ* die gewünschte regionale Ebene spezifiziert&#58;  - 1=Bundesländer,   - 2=Regierungsbezirke und Statistische Regionen,   - 3=Kreise und kreisfreie Städte,  - 5=Gemeinden/Verbandsgemeinde.   Gültige Einträge für die *tableName* werden im Folgenden auszugsweise dargestellt (jeweils mit den enthaltenen Variablen/fields)   - Bevölkerungsdichte&#58; ai002_1_5  - - ai0201&#58; Bevölkerungsdichte (EW je qkm)  - - ai0202&#58; Bevölkerungsentwicklung im Jahr je 10.000 EW  - - ai0208&#58; Anteil der ausländischen Bevölkerung an der Gesamtbevölkerung  - - ai0209&#58; Lebendgeborene je 10.000 EW  - - ai0210&#58; Gestorbene je 10.000 EW  - - ai0211&#58; Geburten-/Gestorbenenüberschuss je 10.000 EW  - - ai0212&#58; Wanderungssaldo je 10.000 EW   - Altersdurchschnitt&#58; ai002_4_5   - - ai0218&#58; Durchschnittsalter der Bevölkerung   - - ai0219&#58; das Durchschnittsalter der Mutter bei der Geburt des 1. Kindes)   - Arbeitslosenquote&#58; ai008_1_5   - - ai0801&#58; Arbeitslosenquote  - - ai0806&#58; Anteil Arbeitslose 15-24 Jahre an Arbeitslosen insgesamt  - - ai0807&#58; Anteil Arbeitslose 55-64 Jahre an Arbeitslosen insgesamt  - - ai0808&#58; Anteil Langzeitarbeitslose an Arbeitslosen insgesamt  - - ai0809&#58; Anteil der ausl. Arbeitslosen an Arbeitslosen insgesamt    - Verfügbares Einkommen je EW&#58; ai_s_01  - SGB-II-Quote&#58; ai_s_04  - BIP je Erwerbstätigem&#58; ai017_1  - Wahlergebnisse Bundestagswahl&#58; ai005' . defaults to "%7B%22source%22%3A%7B%22dataSource%22%3A%7B%22geometryType%22%3A%22esriGeometryPolygon%22%2C%22workspaceId%22%3A%22gdb%22%2C%22query%22%3A%22SELECT%20*%20FROM%20verwaltungsgrenzen_gesamt%20LEFT%20OUTER%20JOIN%20ai002_1_5%20ON%20ags%20%3D%20ags2%20and%20jahr%20%3D%20jahr2%20WHERE%20typ%20%3D%201%20AND%20jahr%20%3D%202020%20AND%20(jahr2%20%3D%202020%20OR%20jahr2%20IS%20NULL)%22%2C%22oidFields%22%3A%22id%22%2C%22spatialReference%22%3A%7B%22wkid%22%3A25832%7D%2C%22type%22%3A%22queryTable%22%7D%2C%22type%22%3A%22dataLayer%22%7D%7D", must be one of ["%7B%22source%22%3A%7B%22dataSource%22%3A%7B%22geometryType%22%3A%22esriGeometryPolygon%22%2C%22workspaceId%22%3A%22gdb%22%2C%22query%22%3A%22SELECT%20*%20FROM%20verwaltungsgrenzen_gesamt%20LEFT%20OUTER%20JOIN%20ai002_1_5%20ON%20ags%20%3D%20ags2%20and%20jahr%20%3D%20jahr2%20WHERE%20typ%20%3D%201%20AND%20jahr%20%3D%202020%20AND%20(jahr2%20%3D%202020%20OR%20jahr2%20IS%20NULL)%22%2C%22oidFields%22%3A%22id%22%2C%22spatialReference%22%3A%7B%22wkid%22%3A25832%7D%2C%22type%22%3A%22queryTable%22%7D%2C%22type%22%3A%22dataLayer%22%7D%7D"]

        Keyword Args:
            out_fields (str): Auszugebende Variablen/fields (z.B. '*').. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            {str: (bool, date, datetime, dict, float, int, list, str, none_type)}
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs["async_req"] = kwargs.get("async_req", False)
        kwargs["_return_http_data_only"] = kwargs.get("_return_http_data_only", True)
        kwargs["_preload_content"] = kwargs.get("_preload_content", True)
        kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
        kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
        kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
        kwargs["_spec_property_naming"] = kwargs.get("_spec_property_naming", False)
        kwargs["_content_type"] = kwargs.get("_content_type")
        kwargs["_host_index"] = kwargs.get("_host_index")
        kwargs["_request_auths"] = kwargs.get("_request_auths", None)
        kwargs["layer"] = layer
        kwargs["f"] = f
        kwargs["return_geometry"] = return_geometry
        kwargs["spatial_rel"] = spatial_rel
        kwargs["where"] = where
        return self.query_endpoint.call_with_http_info(**kwargs)
