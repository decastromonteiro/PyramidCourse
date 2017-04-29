import sqlalchemy
import sqlalchemy.orm
from pyramidcourse.data.modelbase import SqlAlchemyBase

'''
RNC table relationships

. One RNC to multiple LAI
. One RNC to multiple SGSN

'''


class RNC(SqlAlchemyBase):
    __tablename__ = 'RNC'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    rnc_name = sqlalchemy.Column(sqlalchemy.String, unique=True)
    date_added = sqlalchemy.Column(sqlalchemy.DateTime)  # Todo implement lambda function
    rnc_vendor = sqlalchemy.Column(sqlalchemy.String)  # todo dropdown menu to select vendor
    rnc_id = sqlalchemy.Column(sqlalchemy.Integer, unique=True)  # RNC Identifier Number
    dpc = sqlalchemy.Column(sqlalchemy.String, unique=True)  # Destination Point Code
    dpx = sqlalchemy.Column(sqlalchemy.String)  #
    mcc = sqlalchemy.Column(sqlalchemy.String)  # Mobile Country Code
    mnc = sqlalchemy.Column(sqlalchemy.String)  # Mobile Network Code
    rnc_ni = sqlalchemy.Column(sqlalchemy.String)
    iu_flex = sqlalchemy.Column(sqlalchemy.Boolean)  # Support for the Iu Flex Feature
    lai = sqlalchemy.orm.relationship("LocationAreaId", back_populates="rnc_name", cascade='all')
    ran_sharing = sqlalchemy.Column(sqlalchemy.Boolean)  # Support for Ran Sharing
    support_r7_qos = sqlalchemy.Column(sqlalchemy.Boolean)  # Support for 3GPP Release7 QoS
    rab_qos = sqlalchemy.Column(sqlalchemy.Boolean)  # Support for Radio Access Bearer QoS
    rnc_version = sqlalchemy.Column(sqlalchemy.String)  # 3GPP Release of the RNC
    sgsn_name = sqlalchemy.Column(sqlalchemy.String)  # todo backpopulate with sgsn_name
    sgsn_nri = sqlalchemy.Column(sqlalchemy.Integer)  # todo backpopulate with sgsn_nri
    sgsn_opc = sqlalchemy.Column(sqlalchemy.String)  # todo backpopulate with sgsn_opc
    sgsn_opx = sqlalchemy.Column(sqlalchemy.Integer)  # todo backpopulate with sgsn_opx
    sgsn_ni = sqlalchemy.Column(sqlalchemy.String)  # todo backpopulate with sgsn_ni
    sgsn_srn = sqlalchemy.Column(sqlalchemy.Integer)
    sgsn_sn = sqlalchemy.Column(sqlalchemy.Integer)
    sgsn_lnk = sqlalchemy.Column(sqlalchemy.Integer)
    sgsn_pri = sqlalchemy.Column(sqlalchemy.Integer)
    sgsn_let = sqlalchemy.Column(sqlalchemy.String)  # todo backpopulate with sgsn_let
    rnc_let = sqlalchemy.Column(sqlalchemy.String)
    sgsn_lex = sqlalchemy.Column(sqlalchemy.Integer)  # todo backpopulate with sgsn_lex
    sgsn_dex = sqlalchemy.Column(sqlalchemy.Integer)
    sgsn_lsx = sqlalchemy.Column(sqlalchemy.Integer)
    sgsn_det = sqlalchemy.Column(sqlalchemy.String)  # todo backpopulate with sgsn_det
    sgsn_ip1 = sqlalchemy.Column(sqlalchemy.String)
    sgsn_ip2 = sqlalchemy.Column(sqlalchemy.String)
    sgsn_port = sqlalchemy.Column(sqlalchemy.Integer, unique=True)
    rnc_ip1 = sqlalchemy.Column(sqlalchemy.String)
    rnc_ip2 = sqlalchemy.Column(sqlalchemy.String)
    rnc_port = sqlalchemy.Column(sqlalchemy.Integer, unique=True)
    share_type = sqlalchemy.Column(sqlalchemy.String)
    client_server = sqlalchemy.Column(sqlalchemy.String)
    ssnx_ranap = sqlalchemy.Column(sqlalchemy.Integer)
    ssnx_scmg = sqlalchemy.Column(sqlalchemy.Integer)
    slsm = sqlalchemy.Column(
        sqlalchemy.Integer)  # todo implement lambda function to calculate the number of connections
    active = sqlalchemy.Column(sqlalchemy.Boolean)
