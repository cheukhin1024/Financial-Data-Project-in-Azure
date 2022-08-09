# Databricks notebook source
#Example: https://databricks.com/notebooks/segment-p13n//sg_03_clustering.html

from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.pipeline import make_pipeline
from sklearn.metrics import silhouette_score, silhouette_samples
from sklearn.model_selection import train_test_split
from sklearn import metrics

import os

import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.colors

import numpy as np
import pyspark.pandas as ps

#import mlflow.sklearn

# COMMAND ----------

spark.sql("set spark.databricks.delta.autoCompact.enabled = true")

# COMMAND ----------

# MAGIC %sql
# MAGIC 
# MAGIC Use deltabase

# COMMAND ----------


data_test = spark.sql("SELECT AAPL_dateTime, \
                              AA_adjClose \
                       FROM deltabase.aapl_30min_delta \
                       FULL JOIN deltabase.aa_30min_delta ON aapl_30min_delta.AAPL_dateTime = AA_dateTime")

# COMMAND ----------

data = spark.sql("SELECT AAPL_adjClose, \
                         AA_adjClose, \
                         AAL_adjClose, \
                         AAP_adjClose, \
                         A_adjClose, \
                         ABBV_adjClose, \
                         ABC_adjClose, \
                         ABMD_adjClose, \
                         ABT_adjClose, \
                         ACN_adjClose, \
                         ACV_adjClose, \
                         ADBE_adjClose, \
                         ADI_adjClose, \
                         ADM_adjClose, \
                         ADP_adjClose, \
                         ADS_adjClose, \
                         ADSK_adjClose, \
                         ADT_adjClose, \
                         AEE_adjClose, \
                         AEP_adjClose, \
                         AES_adjClose, \
                         AFL_adjClose, \
                         AIG_adjClose, \
                         AINV_adjClose, \
                         AIV_adjClose, \
                         AIZ_adjClose, \
                         AJG_adjClose, \
                         AKAM_adjClose, \
                         ALB_adjClose, \
                         ALGN_adjClose, \
                         ALK_adjClose, \
                         ALL_adjClose, \
                         ALLE_adjClose, \
                         ALTR_adjClose, \
                         AMAT_adjClose, \
                         AMBC_adjClose, \
                         AMCR_adjClose, \
                         AMD_adjClose, \
                         AME_adjClose, \
                         AMG_adjClose, \
                         AMGN_adjClose, \
                         AMP_adjClose, \
                         AMT_adjClose, \
                         AMZN_adjClose \
                         AN_adjClose, \
                         ANET_adjClose, \
                         ANF_adjClose, \
                         ANSS_adjClose, \
                         ANTM_adjClose, \
                         AON_adjClose, \
                         AOS_adjClose, \
                         APA_adjClose, \
                         APD_adjClose, \
                         APH_adjClose, \
                         APTV_adjClose, \
                         ARE_adjClose, \
                         ARNC_adjClose, \
                         ASH_adjClose, \
                         ASO_adjClose, \
                         ATGE_adjClose, \
                         ATI_adjClose, \
                         ATO_adjClose, \
                         ATVI_adjClose, \
                         AVB_adjClose, \
                         AVGO_adjClose, \
                         AVY_adjClose, \
                         AWK_adjClose, \
                         AXP_adjClose, \
                         AYI_adjClose, \
                         AZO_adjClose, \
                         BA_adjClose, \
                         BAC_adjClose, \
                         BAX_adjClose, \
                         BBBY_adjClose, \
                         BBY_adjClose, \
                         BC_adjClose, \
                         BDX_adjClose, \
                         BEN_adjClose, \
                         BFB_adjClose, \
                         BIDU_adjClose, \
                         BIG_adjClose, \
                         BIIB_adjClose, \
                         BIO_adjClose, \
                         BK_adjClose, \
                         BKNG_adjClose, \
                         BLK_adjClose, \
                         BLL_adjClose, \
                         BMRN_adjClose, \
                         BMY_adjClose, \
                         BR_adjClose, \
                         BRKB_adjClose, \
                         BRO_adjClose, \
                         BSX_adjClose, \
                         BTU_adjClose, \
                         BUD_adjClose, \
                         BWA_adjClose, \
                         BXP_adjClose, \
                         C_adjClose, \
                         CAG_adjClose, \
                         CAH_adjClose, \
                         CAR_adjClose, \
                         CARR_adjClose, \
                         CAT_adjClose, \
                         CB_adjClose, \
                         CBH_adjClose, \
                         CBOE_adjClose, \
                         CBRE_adjClose, \
                         CC_adjClose, \
                         CCI_adjClose, \
                         CCK_adjClose, \
                         CCL_adjClose, \
                         CCU_adjClose, \
                         CDAY_adjClose, \
                         CDNS_adjClose, \
                         CDW_adjClose, \
                         CE_adjClose, \
                         CERN_adjClose, \
                         CF_adjClose, \
                         CFG_adjClose, \
                         CHD_adjClose, \
                         CHIR_adjClose, \
                         CHK_adjClose, \
                         CHKP_adjClose, \
                         CHRW_adjClose, \
                         CHTR_adjClose, \
                         CI_adjClose, \
                         CIEN_adjClose, \
                         CINF_adjClose, \
                         CIT_adjClose, \
                         CL_adjClose, \
                         CLF_adjClose, \
                         CLX_adjClose, \
                         CMA_adjClose, \
                         CMCSA_adjClose, \
                         CME_adjClose, \
                         CMG_adjClose, \
                         CMI_adjClose, \
                         CMS_adjClose, \
                         CNC_adjClose, \
                         CNP_adjClose, \
                         CNX_adjClose, \
                         COF_adjClose, \
                         COO_adjClose, \
                         COOP_adjClose, \
                         COP_adjClose, \
                         COST_adjClose, \
                         COTY_adjClose, \
                         CPB_adjClose, \
                         CPRI_adjClose, \
                         CPRT_adjClose, \
                         CPT_adjClose, \
                         CRM_adjClose, \
                         CSCO_adjClose, \
                         CSX_adjClose, \
                         CTAS_adjClose, \
                         CTLT_adjClose, \
                         CTSH_adjClose, \
                         CTVA_adjClose, \
                         CTXS_adjClose, \
                         CVS_adjClose, \
                         CVX_adjClose, \
                         CZR_adjClose, \
                         D_adjClose, \
                         DAL_adjClose, \
                         DAN_adjClose, \
                         DD_adjClose, \
                         DDS_adjClose, \
                         DE_adjClose, \
                         DELL_adjClose, \
                         DFS_adjClose, \
                         DG_adjClose, \
                         DGX_adjClose, \
                         DHI_adjClose, \
                         DHR_adjClose, \
                         DIS_adjClose, \
                         DISCA_adjClose, \
                         DISCK_adjClose, \
                         DISH_adjClose, \
                         DLR_adjClose, \
                         DLTR_adjClose, \
                         DLX_adjClose, \
                         DNB_adjClose, \
                         DOV_adjClose, \
                         DOW_adjClose, \
                         DPZ_adjClose, \
                         DRE_adjClose, \
                         DRI_adjClose, \
                         DTE_adjClose, \
                         DUK_adjClose, \
                         DVA_adjClose, \
                         DVN_adjClose, \
                         DXC_adjClose, \
                         DXCM_adjClose, \
                         EA_adjClose, \
                         EBAY_adjClose, \
                         ECL_adjClose, \
                         ED_adjClose, \
                         EFX_adjClose, \
                         EIX_adjClose, \
                         EL_adjClose, \
                         EMN_adjClose, \
                         EMR_adjClose, \
                         ENDP_adjClose, \
                         ENPH_adjClose, \
                         EOG_adjClose, \
                         EPAM_adjClose, \
                         EQ_adjClose, \
                         EQIX_adjClose, \
                         EQR_adjClose, \
                         EQT_adjClose, \
                         ES_adjClose, \
                         ESS_adjClose, \
                         ETN_adjClose, \
                         ETR_adjClose, \
                         ETSY_adjClose, \
                         EVRG_adjClose, \
                         EW_adjClose, \
                         EXC_adjClose, \
                         EXPD_adjClose, \
                         EXPE_adjClose, \
                         EXR_adjClose, \
                         F_adjClose, \
                         FANG_adjClose, \
                         FAST_adjClose, \
                         FB_adjClose, \
                         FBHS_adjClose, \
                         FCX_adjClose, \
                         FDS_adjClose, \
                         FDX_adjClose, \
                         FE_adjClose, \
                         FFIV_adjClose, \
                         FFHN_adjClose, \
                         FIS_adjClose, \
                         FISV_adjClose, \
                         FITB_adjClose, \
                         FL_adjClose, \
                         FLEX_adjClose \
                         FLR_adjClose, \
                         FLS_adjClose, \
                         FLT_adjClose, \
                         FMC_adjClose, \
                         FOSL_adjClose, \
                         FOX_adjClose, \
                         FOXA_adjClose, \
                         FPL_adjClose, \
                         FRC_adjClose, \
                         FRT_adjClose, \
                         FSLR_adjClose, \
                         FTI_adjClose, \
                         FTNT_adjClose, \
                         FTV_adjClose, \
                         GCI_adjClose, \
                         GD_adjClose, \
                         GE_adjClose, \
                         GHC_adjClose, \
                         GILD_adjClose, \
                         GIS_adjClose, \
                         GL_adjClose, \
                         GLW_adjClose, \
                         GM_adjClose, \
                         GME_adjClose, \
                         GNRC_adjClose, \
                         GNW_adjClose, \
                         GOOG_adjClose, \
                         GOOGL_adjClose, \
                         GP_adjClose, \
                         GPC_adjClose, \
                         GPN_adjClose, \
                         GPS_adjClose, \
                         GRMN_adjClose, \
                         GS_adjClose, \
                         GT_adjClose, \
                         GWW_adjClose, \
                         HAL_adjClose, \
                         HAS_adjClose, \
                         HBAN_adjClose, \
                         HBI_adjClose, \
                         HCA_adjClose, \
                         HD_adjClose, \
                         HES_adjClose, \
                         HFC_adjClose, \
                         HIG_adjClose, \
                         HII_adjClose, \
                         HLT_adjClose, \
                         HOG_adjClose, \
                         HOLX_adjClose, \
                         HON_adjClose, \
                         HP_adjClose, \
                         HPE_adjClose, \
                         HPQ_adjClose, \
                         HRB_adjClose, \
                         HRL_adjClose, \
                         HSIC_adjClose, \
                         HST_adjClose, \
                         HSY_adjClose, \
                         HUM_adjClose, \
                         IAC_adjClose, \
                         IBM_adjClose, \
                         ICE_adjClose, \
                         IDXX_adjClose, \
                         IEX_adjClose, \
                         IFF_adjClose, \
                         IGT_adjClose, \
                         IHRT_adjClose, \
                         ILMN_adjClose, \
                         INCY_adjClose, \
                         INFO_adjClose \
                         INFY_adjClose, \
                         INTC_adjClose, \
                         INTU_adjClose, \
                         IP_adjClose, \
                         IPG_adjClose, \
                         IPGP_adjClose, \
                         IQV_adjClose, \
                         IR_adjClose, \
                         IRM_adjClose, \
                         ISRG_adjClose, \
                         IT_adjClose, \
                         ITT_adjClose, \
                         ITW_adjClose, \
                         IVZ_adjClose, \
                         J_adjClose, \
                         JBHT_adjClose, \
                         JBL_adjClose, \
                         JCI_adjClose, \
                         JD_adjClose, \
                         JEF_adjClose, \
                         JKHY_adjClose, \
                         JNJ_adjClose, \
                         JNPR_adjClose, \
                         JP_adjClose, \
                         JPM_adjClose, \
                         JWN_adjClose, \
                         K_adjClose, \
                         KBH_adjClose, \
                         KEY_adjClose, \
                         KEYS_adjClose, \
                         KHC_adjClose, \
                         KIM_adjClose, \
                         KLAC_adjClose, \
                         KMB_adjClose, \
                         KMI_adjClose, \
                         KMX_adjClose, \
                         KO_adjClose, \
                         KODK_adjClose, \
                         KR_adjClose, \
                         KSS_adjClose, \
                         KSU_adjClose, \
                         L_adjClose, \
                         LBTYK_adjClose, \
                         LDOS_adjClose, \
                         LEG_adjClose, \
                         LEN_adjClose, \
                         LH_adjClose, \
                         LHX_adjClose, \
                         LIFE_adjClose, \
                         LIN_adjClose, \
                         LKQ_adjClose, \
                         LLY_adjClose, \
                         LMT_adjClose, \
                         LNC_adjClose, \
                         LNT_adjClose, \
                         LOGI_adjClose, \
                         LOW_adjClose, \
                         LRCX_adjClose, \
                         LSI_adjClose, \
                         LU_adjClose, \
                         LUMN_adjClose, \
                         LUV_adjClose, \
                         LVS_adjClose, \
                         LW_adjClose, \
                         LYB_adjClose, \
                         LYV_adjClose, \
                         M_adjClose, \
                         MA_adjClose, \
                         MAA_adjClose, \
                         MAC_adjClose, \
                         MAR_adjClose, \
                         MAS_adjClose, \
                         MAT_adjClose, \
                         MBI_adjClose, \
                         MCD_adjClose, \
                         MCHP_adjClose, \
                         MCK_adjClose, \
                         MCO_adjClose, \
                         MDLZ_adjClose, \
                         MDP_adjClose, \
                         MDT_adjClose, \
                         MET_adjClose, \
                         MGM_adjClose, \
                         MHK_adjClose, \
                         MKC_adjClose \
                         MKTX_adjClose, \
                         MLM_adjClose, \
                         MMC_adjClose, \
                         MMI_adjClose, \
                         MMM_adjClose, \
                         MNST_adjClose, \
                         MO_adjClose, \
                         MOH_adjClose, \
                         MOS_adjClose, \
                         MPC_adjClose, \
                         MPWR_adjClose, \
                         MRK_adjClose, \
                         MRO_adjClose, \
                         MRVL_adjClose, \
                         MS_adjClose, \
                         MSCI_adjClose, \
                         MSFT_adjClose, \
                         MSI_adjClose, \
                         MTB_adjClose, \
                         MTCH_adjClose, \
                         MTD_adjClose, \
                         MTW_adjClose, \
                         MU_adjClose, \
                         MUR_adjClose, \
                         NAVI_adjClose, \
                         NBR_adjClose, \
                         NCLH_adjClose, \
                         NDAQ_adjClose, \
                         NDSN_adjClose, \
                         NE_adjClose, \
                         NEE_adjClose, \
                         NEM_adjClose, \
                         NFLX_adjClose, \
                         NI_adjClose, \
                         NKE_adjClose, \
                         NKTR_adjClose, \
                         NLOK_adjClose, \
                         NLSN_adjClose, \
                         NOC_adjClose, \
                         NOV_adjClose, \
                         NOW_adjClose, \
                         NRG_adjClose, \
                         NSC_adjClose, \
                         NTAP_adjClose, \
                         NTES_adjClose, \
                         NTRS_adjClose, \
                         NUE_adjClose, \
                         NVDA_adjClose, \
                         NVR_adjClose, \
                         NWL_adjClose, \
                         NWS_adjClose, \
                         NWSA_adjClose, \
                         NXPI_adjClose, \
                         NYT_adjClose, \
                         O_adjClose, \
                         ODFL_adjClose, \
                         ODP_adjClose, \
                         OGN_adjClose, \
                         OI_adjClose, \
                         OKE_adjClose, \
                         OMC_adjClose, \
                         ONE_adjClose, \
                         ORCL_adjClose, \
                         ORLY_adjClose, \
                         OTIS_adjClose, \
                         OXY_adjClose, \
                         PAR_adjClose, \
                         PAYC_adjClose, \
                         PAYX_adjClose, \
                         PBCT_adjClose \
                         PBI_adjClose, \
                         PCAR_adjClose, \
                         PCG_adjClose, \
                         PDCO_adjClose, \
                         PEAK_adjClose, \
                         PEG_adjClose, \
                         PENN_adjClose, \
                         PEP_adjClose, \
                         PFE_adjClose, \
                         PFG_adjClose, \
                         PG_adjClose, \
                         PGR_adjClose, \
                         PH_adjClose, \
                         PHM_adjClose, \
                         PKG_adjClose, \
                         PKI_adjClose, \
                         PLD_adjClose, \
                         PLL_adjClose, \
                         PM_adjClose, \
                         PNC_adjClose, \
                         PNR_adjClose, \
                         PNW_adjClose, \
                         POOL_adjClose, \
                         PPG_adjClose, \
                         PPL_adjClose, \
                         PRGO_adjClose, \
                         PRI_adjClose, \
                         PRU_adjClose, \
                         PSA_adjClose, \
                         PSX_adjClose, \
                         PTC_adjClose, \
                         PVH_adjClose, \
                         PWR_adjClose, \
                         PXD_adjClose, \
                         PYPL_adjClose, \
                         QCOM_adjClose, \
                         QGEN_adjClose, \
                         QRVO_adjClose, \
          FROM deltabase.aapl_30min_delta \
     FULL JOIN deltabase.aa_30min_delta ON aapl_30min_delta.AAPL_dateTime = AA_dateTime \
     FULL JOIN deltabase.aal_30min_delta ON aapl_30min_delta.AAPL_dateTime = AAL_dateTime \
     FULL JOIN deltabase.aap_30min_delta ON aapl_30min_delta.AAPL_dateTime = AAP_dateTime \
     FULL JOIN deltabase.a_30min_delta ON aapl_30min_delta.AAPL_dateTime = A_dateTime \
     FULL JOIN deltabase.abbv_30min_delta ON aapl_30min_delta.AAPL_dateTime = ABBV_dateTime \
     FULL JOIN deltabase.abc_30min_delta ON aapl_30min_delta.AAPL_dateTime = ABC_dateTime \
     FULL JOIN deltabase.abmd_30min_delta ON aapl_30min_delta.AAPL_dateTime = ABMD_dateTime \
     FULL JOIN deltabase.abt_30min_delta ON aapl_30min_delta.AAPL_dateTime = ABT_dateTime \
     FULL JOIN deltabase.acn_30min_delta ON aapl_30min_delta.AAPL_dateTime = ACN_dateTime \
     FULL JOIN deltabase.acv_30min_delta ON aapl_30min_delta.AAPL_dateTime = ACV_dateTime \
     FULL JOIN deltabase.adbe_30min_delta ON aapl_30min_delta.AAPL_dateTime = ADBE_dateTime \
     FULL JOIN deltabase.adi_30min_delta ON aapl_30min_delta.AAPL_dateTime = ADI_dateTime \
     FULL JOIN deltabase.adm_30min_delta ON aapl_30min_delta.AAPL_dateTime = ADM_dateTime \
     FULL JOIN deltabase.adp_30min_delta ON aapl_30min_delta.AAPL_dateTime = ADP_dateTime \
     FULL JOIN deltabase.ads_30min_delta ON aapl_30min_delta.AAPL_dateTime = ADS_dateTime \
     FULL JOIN deltabase.adsk_30min_delta ON aapl_30min_delta.AAPL_dateTime = ADSK_dateTime \
     FULL JOIN deltabase.adt_30min_delta ON aapl_30min_delta.AAPL_dateTime = ADT_dateTime \
     FULL JOIN deltabase.aee_30min_delta ON aapl_30min_delta.AAPL_dateTime = AEE_dateTime \
     FULL JOIN deltabase.aep_30min_delta ON aapl_30min_delta.AAPL_dateTime = AEP_dateTime \
     FULL JOIN deltabase.aes_30min_delta ON aapl_30min_delta.AAPL_dateTime = AES_dateTime \
     FULL JOIN deltabase.afl_30min_delta ON aapl_30min_delta.AAPL_dateTime = AFL_dateTime \
     FULL JOIN deltabase.aig_30min_delta ON aapl_30min_delta.AAPL_dateTime = AIG_dateTime \
     FULL JOIN deltabase.ainv_30min_delta ON aapl_30min_delta.AAPL_dateTime = AINV_dateTime \
     FULL JOIN deltabase.aiv_30min_delta ON aapl_30min_delta.AAPL_dateTime = AIV_dateTime \
     FULL JOIN deltabase.aiz_30min_delta ON aapl_30min_delta.AAPL_dateTime = AIZ_dateTime \
     FULL JOIN deltabase.ajg_30min_delta ON aapl_30min_delta.AAPL_dateTime = AJG_dateTime \
     FULL JOIN deltabase.akam_30min_delta ON aapl_30min_delta.AAPL_dateTime = AKAM_dateTime \
     FULL JOIN deltabase.alb_30min_delta ON aapl_30min_delta.AAPL_dateTime = ALB_dateTime \
     FULL JOIN deltabase.algn_30min_delta ON aapl_30min_delta.AAPL_dateTime = ALGN_dateTime \
     FULL JOIN deltabase.alk_30min_delta ON aapl_30min_delta.AAPL_dateTime = ALK_dateTime \
     FULL JOIN deltabase.all_30min_delta ON aapl_30min_delta.AAPL_dateTime = ALL_dateTime \
     FULL JOIN deltabase.alle_30min_delta ON aapl_30min_delta.AAPL_dateTime = ALLE_dateTime \
     FULL JOIN deltabase.altr_30min_delta ON aapl_30min_delta.AAPL_dateTime = ALTR_dateTime \
     FULL JOIN deltabase.amat_30min_delta ON aapl_30min_delta.AAPL_dateTime = AMAT_dateTime \
     FULL JOIN deltabase.ambc_30min_delta ON aapl_30min_delta.AAPL_dateTime = AMBC_dateTime \
     FULL JOIN deltabase.amcr_30min_delta ON aapl_30min_delta.AAPL_dateTime = AMCR_dateTime \
     FULL JOIN deltabase.amd_30min_delta ON aapl_30min_delta.AAPL_dateTime = AMD_dateTime \
     FULL JOIN deltabase.ame_30min_delta ON aapl_30min_delta.AAPL_dateTime = AME_dateTime \
     FULL JOIN deltabase.amg_30min_delta ON aapl_30min_delta.AAPL_dateTime = AMG_dateTime \
     FULL JOIN deltabase.amgn_30min_delta ON aapl_30min_delta.AAPL_dateTime = AMGN_dateTime \
     FULL JOIN deltabase.amp_30min_delta ON aapl_30min_delta.AAPL_dateTime = AMP_dateTime \
     FULL JOIN deltabase.amt_30min_delta ON aapl_30min_delta.AAPL_dateTime = AMT_dateTime \
     FULL JOIN deltabase.amzn_30min_delta ON aapl_30min_delta.AAPL_dateTime = AMZN_dateTime \
     FULL JOIN deltabase.an_30min_delta ON aapl_30min_delta.AAPL_dateTime = AN_dateTime \
     FULL JOIN deltabase.anet_30min_delta ON aapl_30min_delta.AAPL_dateTime = ANET_dateTime \
     FULL JOIN deltabase.anf_30min_delta ON aapl_30min_delta.AAPL_dateTime = ANF_dateTime \
     FULL JOIN deltabase.anss_30min_delta ON aapl_30min_delta.AAPL_dateTime = ANSS_dateTime \
     FULL JOIN deltabase.antm_30min_delta ON aapl_30min_delta.AAPL_dateTime = ANTM_dateTime \
     FULL JOIN deltabase.aon_30min_delta ON aapl_30min_delta.AAPL_dateTime = AON_dateTime \
     FULL JOIN deltabase.aos_30min_delta ON aapl_30min_delta.AAPL_dateTime = AOS_dateTime \
     FULL JOIN deltabase.apa_30min_delta ON aapl_30min_delta.AAPL_dateTime = APA_dateTime \
     FULL JOIN deltabase.apd_30min_delta ON aapl_30min_delta.AAPL_dateTime = APD_dateTime \
     FULL JOIN deltabase.aph_30min_delta ON aapl_30min_delta.AAPL_dateTime = APH_dateTime \
     FULL JOIN deltabase.aptv_30min_delta ON aapl_30min_delta.AAPL_dateTime = APTV_dateTime \
     FULL JOIN deltabase.are_30min_delta ON aapl_30min_delta.AAPL_dateTime = ARE_dateTime \
     FULL JOIN deltabase.arnc_30min_delta ON aapl_30min_delta.AAPL_dateTime = ARNC_dateTime \
     FULL JOIN deltabase.ash_30min_delta ON aapl_30min_delta.AAPL_dateTime = ASH_dateTime \
     FULL JOIN deltabase.aso_30min_delta ON aapl_30min_delta.AAPL_dateTime = ASO_dateTime \
     FULL JOIN deltabase.atge_30min_delta ON aapl_30min_delta.AAPL_dateTime = ATGE_dateTime \
     FULL JOIN deltabase.ati_30min_delta ON aapl_30min_delta.AAPL_dateTime = ATI_dateTime \
     FULL JOIN deltabase.ato_30min_delta ON aapl_30min_delta.AAPL_dateTime = ATO_dateTime \
     FULL JOIN deltabase.atvi_30min_delta ON aapl_30min_delta.AAPL_dateTime = ATVI_dateTime \
     FULL JOIN deltabase.avb_30min_delta ON aapl_30min_delta.AAPL_dateTime = AVB_dateTime \
     FULL JOIN deltabase.avgo_30min_delta ON aapl_30min_delta.AAPL_dateTime = AVGO_dateTime \
     FULL JOIN deltabase.avy_30min_delta ON aapl_30min_delta.AAPL_dateTime = AVY_dateTime \
     FULL JOIN deltabase.awk_30min_delta ON aapl_30min_delta.AAPL_dateTime = AWK_dateTime \
     FULL JOIN deltabase.axp_30min_delta ON aapl_30min_delta.AAPL_dateTime = AXP_dateTime \
     FULL JOIN deltabase.ayi_30min_delta ON aapl_30min_delta.AAPL_dateTime = AYI_dateTime \
     FULL JOIN deltabase.azo_30min_delta ON aapl_30min_delta.AAPL_dateTime = AZO_dateTime \
     FULL JOIN deltabase.ba_30min_delta ON aapl_30min_delta.AAPL_dateTime = BA_dateTime \
     FULL JOIN deltabase.bac_30min_delta ON aapl_30min_delta.AAPL_dateTime = BAC_dateTime \
     FULL JOIN deltabase.bax_30min_delta ON aapl_30min_delta.AAPL_dateTime = BAX_dateTime \
     FULL JOIN deltabase.bbby_30min_delta ON aapl_30min_delta.AAPL_dateTime = BBBY_dateTime \
     FULL JOIN deltabase.bby_30min_delta ON aapl_30min_delta.AAPL_dateTime = BBY_dateTime \
     FULL JOIN deltabase.bc_30min_delta ON aapl_30min_delta.AAPL_dateTime = BC_dateTime \
     FULL JOIN deltabase.bdx_30min_delta ON aapl_30min_delta.AAPL_dateTime = BDX_dateTime \
     FULL JOIN deltabase.ben_30min_delta ON aapl_30min_delta.AAPL_dateTime = BEN_dateTime \
     FULL JOIN deltabase.bfb_30min_delta ON aapl_30min_delta.AAPL_dateTime = BFB_dateTime \
     FULL JOIN deltabase.bidu_30min_delta ON aapl_30min_delta.AAPL_dateTime = BIDU_dateTime \
     FULL JOIN deltabase.big_30min_delta ON aapl_30min_delta.AAPL_dateTime = BIG_dateTime \
     FULL JOIN deltabase.biib_30min_delta ON aapl_30min_delta.AAPL_dateTime = BIIB_dateTime \
     FULL JOIN deltabase.bio_30min_delta ON aapl_30min_delta.AAPL_dateTime = BIO_dateTime \
     FULL JOIN deltabase.bk_30min_delta ON aapl_30min_delta.AAPL_dateTime = BK_dateTime \
     FULL JOIN deltabase.bkng_30min_delta ON aapl_30min_delta.AAPL_dateTime = BKNG_dateTime \
     FULL JOIN deltabase.blk_30min_delta ON aapl_30min_delta.AAPL_dateTime = BLK_dateTime \
     FULL JOIN deltabase.bll_30min_delta ON aapl_30min_delta.AAPL_dateTime = BLL_dateTime \
     FULL JOIN deltabase.bmrn_30min_delta ON aapl_30min_delta.AAPL_dateTime = BMRN_dateTime \
     FULL JOIN deltabase.bmy_30min_delta ON aapl_30min_delta.AAPL_dateTime = BMY_dateTime \
     FULL JOIN deltabase.br_30min_delta ON aapl_30min_delta.AAPL_dateTime = BR_dateTime \
     FULL JOIN deltabase.brkb_30min_delta ON aapl_30min_delta.AAPL_dateTime = BRKB_dateTime \
     FULL JOIN deltabase.bro_30min_delta ON aapl_30min_delta.AAPL_dateTime = BRO_dateTime \
     FULL JOIN deltabase.bsx_30min_delta ON aapl_30min_delta.AAPL_dateTime = BSX_dateTime \
     FULL JOIN deltabase.btu_30min_delta ON aapl_30min_delta.AAPL_dateTime = BTU_dateTime \
     FULL JOIN deltabase.bud_30min_delta ON aapl_30min_delta.AAPL_dateTime = BUD_dateTime \
     FULL JOIN deltabase.bwa_30min_delta ON aapl_30min_delta.AAPL_dateTime = BWA_dateTime \
     FULL JOIN deltabase.bxp_30min_delta ON aapl_30min_delta.AAPL_dateTime = BXP_dateTime \
     FULL JOIN deltabase.c_30min_delta ON aapl_30min_delta.AAPL_dateTime = C_dateTime \
     FULL JOIN deltabase.cag_30min_delta ON aapl_30min_delta.AAPL_dateTime = CAG_dateTime \
     FULL JOIN deltabase.cah_30min_delta ON aapl_30min_delta.AAPL_dateTime = CAH_dateTime \
     FULL JOIN deltabase.car_30min_delta ON aapl_30min_delta.AAPL_dateTime = CAR_dateTime \
     FULL JOIN deltabase.carr_30min_delta ON aapl_30min_delta.AAPL_dateTime = CARR_dateTime \
     FULL JOIN deltabase.cat_30min_delta ON aapl_30min_delta.AAPL_dateTime = CAT_dateTime \
     FULL JOIN deltabase.cb_30min_delta ON aapl_30min_delta.AAPL_dateTime = CB_dateTime \
     FULL JOIN deltabase.cbh_30min_delta ON aapl_30min_delta.AAPL_dateTime = CBH_dateTime \
     FULL JOIN deltabase.cboe_30min_delta ON aapl_30min_delta.AAPL_dateTime = CBOE_dateTime \
     FULL JOIN deltabase.cbre_30min_delta ON aapl_30min_delta.AAPL_dateTime = CBRE_dateTime \
     FULL JOIN deltabase.cc_30min_delta ON aapl_30min_delta.AAPL_dateTime = CC_dateTime \
     FULL JOIN deltabase.cci_30min_delta ON aapl_30min_delta.AAPL_dateTime = CCI_dateTime \
     FULL JOIN deltabase.cck_30min_delta ON aapl_30min_delta.AAPL_dateTime = CCK_dateTime \
     FULL JOIN deltabase.ccl_30min_delta ON aapl_30min_delta.AAPL_dateTime = CCL_dateTime \
     FULL JOIN deltabase.ccu_30min_delta ON aapl_30min_delta.AAPL_dateTime = CCU_dateTime \
     FULL JOIN deltabase.cday_30min_delta ON aapl_30min_delta.AAPL_dateTime = CDAY_dateTime \
     FULL JOIN deltabase.cdns_30min_delta ON aapl_30min_delta.AAPL_dateTime = CDNS_dateTime \
     FULL JOIN deltabase.cdw_30min_delta ON aapl_30min_delta.AAPL_dateTime = CDW_dateTime \
     FULL JOIN deltabase.ce_30min_delta ON aapl_30min_delta.AAPL_dateTime = CE_dateTime \
     FULL JOIN deltabase.cern_30min_delta ON aapl_30min_delta.AAPL_dateTime = CERN_dateTime \
     FULL JOIN deltabase.cf_30min_delta ON aapl_30min_delta.AAPL_dateTime = CF_dateTime \
     FULL JOIN deltabase.cfg_30min_delta ON aapl_30min_delta.AAPL_dateTime = CFG_dateTime \
     FULL JOIN deltabase.chd_30min_delta ON aapl_30min_delta.AAPL_dateTime = CHD_dateTime \
     FULL JOIN deltabase.chir_30min_delta ON aapl_30min_delta.AAPL_dateTime = CHIR_dateTime \
     FULL JOIN deltabase.chk_30min_delta ON aapl_30min_delta.AAPL_dateTime = CHK_dateTime \
     FULL JOIN deltabase.chkp_30min_delta ON aapl_30min_delta.AAPL_dateTime = CHKP_dateTime \
     FULL JOIN deltabase.chrw_30min_delta ON aapl_30min_delta.AAPL_dateTime = CHRW_dateTime \
     FULL JOIN deltabase.chtr_30min_delta ON aapl_30min_delta.AAPL_dateTime = CHTR_dateTime \
     FULL JOIN deltabase.ci_30min_delta ON aapl_30min_delta.AAPL_dateTime = CI_dateTime \
     FULL JOIN deltabase.cien_30min_delta ON aapl_30min_delta.AAPL_dateTime = CIEN_dateTime \
     FULL JOIN deltabase.cinf_30min_delta ON aapl_30min_delta.AAPL_dateTime = CINF_dateTime \
     FULL JOIN deltabase.cit_30min_delta ON aapl_30min_delta.AAPL_dateTime = CIT_dateTime \
     FULL JOIN deltabase.cl_30min_delta ON aapl_30min_delta.AAPL_dateTime = CL_dateTime \
     FULL JOIN deltabase.clf_30min_delta ON aapl_30min_delta.AAPL_dateTime = CLF_dateTime \
     FULL JOIN deltabase.clx_30min_delta ON aapl_30min_delta.AAPL_dateTime = CLX_dateTime \
     FULL JOIN deltabase.cma_30min_delta ON aapl_30min_delta.AAPL_dateTime = CMA_dateTime \
     FULL JOIN deltabase.cmcsa_30min_delta ON aapl_30min_delta.AAPL_dateTime = CMCSA_dateTime \
     FULL JOIN deltabase.cme_30min_delta ON aapl_30min_delta.AAPL_dateTime = CME_dateTime \
     FULL JOIN deltabase.cmg_30min_delta ON aapl_30min_delta.AAPL_dateTime = CMG_dateTime \
     FULL JOIN deltabase.cmi_30min_delta ON aapl_30min_delta.AAPL_dateTime = CMI_dateTime \
     FULL JOIN deltabase.cms_30min_delta ON aapl_30min_delta.AAPL_dateTime = CMS_dateTime \
     FULL JOIN deltabase.cnc_30min_delta ON aapl_30min_delta.AAPL_dateTime = CNC_dateTime \
     FULL JOIN deltabase.cnp_30min_delta ON aapl_30min_delta.AAPL_dateTime = CNP_dateTime \
     FULL JOIN deltabase.cnx_30min_delta ON aapl_30min_delta.AAPL_dateTime = CNX_dateTime \
     FULL JOIN deltabase.cof_30min_delta ON aapl_30min_delta.AAPL_dateTime = COF_dateTime \
     FULL JOIN deltabase.coo_30min_delta ON aapl_30min_delta.AAPL_dateTime = COO_dateTime \
     FULL JOIN deltabase.coop_30min_delta ON aapl_30min_delta.AAPL_dateTime = COOP_dateTime \
     FULL JOIN deltabase.cop_30min_delta ON aapl_30min_delta.AAPL_dateTime = COP_dateTime \
     FULL JOIN deltabase.cost_30min_delta ON aapl_30min_delta.AAPL_dateTime = COST_dateTime \
     FULL JOIN deltabase.coty_30min_delta ON aapl_30min_delta.AAPL_dateTime = COTY_dateTime \
     FULL JOIN deltabase.cpb_30min_delta ON aapl_30min_delta.AAPL_dateTime = CPB_dateTime \
     FULL JOIN deltabase.cpri_30min_delta ON aapl_30min_delta.AAPL_dateTime = CPRI_dateTime \
     FULL JOIN deltabase.cprt_30min_delta ON aapl_30min_delta.AAPL_dateTime = CPRT_dateTime \
     FULL JOIN deltabase.cpt_30min_delta ON aapl_30min_delta.AAPL_dateTime = CPT_dateTime \
     FULL JOIN deltabase.crm_30min_delta ON aapl_30min_delta.AAPL_dateTime = CRM_dateTime \
     FULL JOIN deltabase.csco_30min_delta ON aapl_30min_delta.AAPL_dateTime = CSCO_dateTime \
     FULL JOIN deltabase.csx_30min_delta ON aapl_30min_delta.AAPL_dateTime = CSX_dateTime \
     FULL JOIN deltabase.ctas_30min_delta ON aapl_30min_delta.AAPL_dateTime = CTAS_dateTime \
     FULL JOIN deltabase.ctlt_30min_delta ON aapl_30min_delta.AAPL_dateTime = CTLT_dateTime \
     FULL JOIN deltabase.ctsh_30min_delta ON aapl_30min_delta.AAPL_dateTime = CTSH_dateTime \
     FULL JOIN deltabase.ctva_30min_delta ON aapl_30min_delta.AAPL_dateTime = CTVA_dateTime \
     FULL JOIN deltabase.ctxs_30min_delta ON aapl_30min_delta.AAPL_dateTime = CTXS_dateTime \
     FULL JOIN deltabase.cvs_30min_delta ON aapl_30min_delta.AAPL_dateTime = CVS_dateTime \
     FULL JOIN deltabase.cvx_30min_delta ON aapl_30min_delta.AAPL_dateTime = CVX_dateTime \
     FULL JOIN deltabase.czr_30min_delta ON aapl_30min_delta.AAPL_dateTime = CZR_dateTime \
     FULL JOIN deltabase.d_30min_delta ON aapl_30min_delta.AAPL_dateTime = D_dateTime \
     FULL JOIN deltabase.dal_30min_delta ON aapl_30min_delta.AAPL_dateTime = DAL_dateTime \
     FULL JOIN deltabase.dan_30min_delta ON aapl_30min_delta.AAPL_dateTime = DAN_dateTime \
     FULL JOIN deltabase.dd_30min_delta ON aapl_30min_delta.AAPL_dateTime = DD_dateTime \
     FULL JOIN deltabase.dds_30min_delta ON aapl_30min_delta.AAPL_dateTime = DDS_dateTime \
     FULL JOIN deltabase.de_30min_delta ON aapl_30min_delta.AAPL_dateTime = DE_dateTime \
     FULL JOIN deltabase.dell_30min_delta ON aapl_30min_delta.AAPL_dateTime = DELL_dateTime \
     FULL JOIN deltabase.dfs_30min_delta ON aapl_30min_delta.AAPL_dateTime = DFS_dateTime \
     FULL JOIN deltabase.dg_30min_delta ON aapl_30min_delta.AAPL_dateTime = DG_dateTime \
     FULL JOIN deltabase.dgx_30min_delta ON aapl_30min_delta.AAPL_dateTime = DGX_dateTime \
     FULL JOIN deltabase.dhi_30min_delta ON aapl_30min_delta.AAPL_dateTime = DHI_dateTime \
     FULL JOIN deltabase.dhr_30min_delta ON aapl_30min_delta.AAPL_dateTime = DHR_dateTime \
     FULL JOIN deltabase.dis_30min_delta ON aapl_30min_delta.AAPL_dateTime = DIS_dateTime \
     FULL JOIN deltabase.disca_30min_delta ON aapl_30min_delta.AAPL_dateTime = DISCA_dateTime \
     FULL JOIN deltabase.disck_30min_delta ON aapl_30min_delta.AAPL_dateTime = DISCK_dateTime \
     FULL JOIN deltabase.dish_30min_delta ON aapl_30min_delta.AAPL_dateTime = DISH_dateTime \
     FULL JOIN deltabase.dlr_30min_delta ON aapl_30min_delta.AAPL_dateTime = DLR_dateTime \
     FULL JOIN deltabase.dltr_30min_delta ON aapl_30min_delta.AAPL_dateTime = DLTR_dateTime \
     FULL JOIN deltabase.dlx_30min_delta ON aapl_30min_delta.AAPL_dateTime = DLX_dateTime \
     FULL JOIN deltabase.dnb_30min_delta ON aapl_30min_delta.AAPL_dateTime = DNB_dateTime \
     FULL JOIN deltabase.dov_30min_delta ON aapl_30min_delta.AAPL_dateTime = DOV_dateTime \
     FULL JOIN deltabase.dow_30min_delta ON aapl_30min_delta.AAPL_dateTime = DOW_dateTime \
     FULL JOIN deltabase.dpz_30min_delta ON aapl_30min_delta.AAPL_dateTime = DPZ_dateTime \
     FULL JOIN deltabase.dre_30min_delta ON aapl_30min_delta.AAPL_dateTime = DRE_dateTime \
     FULL JOIN deltabase.dri_30min_delta ON aapl_30min_delta.AAPL_dateTime = DRI_dateTime \
     FULL JOIN deltabase.dte_30min_delta ON aapl_30min_delta.AAPL_dateTime = DTE_dateTime \
     FULL JOIN deltabase.duk_30min_delta ON aapl_30min_delta.AAPL_dateTime = DUK_dateTime \
     FULL JOIN deltabase.dva_30min_delta ON aapl_30min_delta.AAPL_dateTime = DVA_dateTime \
     FULL JOIN deltabase.dvn_30min_delta ON aapl_30min_delta.AAPL_dateTime = DVN_dateTime \
     FULL JOIN deltabase.dxc_30min_delta ON aapl_30min_delta.AAPL_dateTime = DXC_dateTime \
     FULL JOIN deltabase.dxcm_30min_delta ON aapl_30min_delta.AAPL_dateTime = DXCM_dateTime \
     FULL JOIN deltabase.ea_30min_delta ON aapl_30min_delta.AAPL_dateTime = EA_dateTime \
     FULL JOIN deltabase.ebay_30min_delta ON aapl_30min_delta.AAPL_dateTime = EBAY_dateTime \
     FULL JOIN deltabase.ecl_30min_delta ON aapl_30min_delta.AAPL_dateTime = ECL_dateTime \
     FULL JOIN deltabase.ed_30min_delta ON aapl_30min_delta.AAPL_dateTime = ED_dateTime \
     FULL JOIN deltabase.efx_30min_delta ON aapl_30min_delta.AAPL_dateTime = EFX_dateTime \
     FULL JOIN deltabase.eix_30min_delta ON aapl_30min_delta.AAPL_dateTime = EIX_dateTime \
     FULL JOIN deltabase.el_30min_delta ON aapl_30min_delta.AAPL_dateTime = EL_dateTime \
     FULL JOIN deltabase.emn_30min_delta ON aapl_30min_delta.AAPL_dateTime = EMN_dateTime \
     FULL JOIN deltabase.emr_30min_delta ON aapl_30min_delta.AAPL_dateTime = EMR_dateTime \
     FULL JOIN deltabase.endp_30min_delta ON aapl_30min_delta.AAPL_dateTime = ENDP_dateTime \
     FULL JOIN deltabase.enph_30min_delta ON aapl_30min_delta.AAPL_dateTime = ENPH_dateTime \
     FULL JOIN deltabase.eog_30min_delta ON aapl_30min_delta.AAPL_dateTime = EOG_dateTime \
     FULL JOIN deltabase.epam_30min_delta ON aapl_30min_delta.AAPL_dateTime = EPAM_dateTime \
     FULL JOIN deltabase.eq_30min_delta ON aapl_30min_delta.AAPL_dateTime = EQ_dateTime \
     FULL JOIN deltabase.eqix_30min_delta ON aapl_30min_delta.AAPL_dateTime = EQIX_dateTime \
     FULL JOIN deltabase.eqr_30min_delta ON aapl_30min_delta.AAPL_dateTime = EQR_dateTime \
     FULL JOIN deltabase.eqt_30min_delta ON aapl_30min_delta.AAPL_dateTime = EQT_dateTime \
     FULL JOIN deltabase.es_30min_delta ON aapl_30min_delta.AAPL_dateTime = ES_dateTime \
     FULL JOIN deltabase.ess_30min_delta ON aapl_30min_delta.AAPL_dateTime = ESS_dateTime \
     FULL JOIN deltabase.etn_30min_delta ON aapl_30min_delta.AAPL_dateTime = ETN_dateTime \
     FULL JOIN deltabase.etr_30min_delta ON aapl_30min_delta.AAPL_dateTime = ETR_dateTime \
     FULL JOIN deltabase.etsy_30min_delta ON aapl_30min_delta.AAPL_dateTime = ETSY_dateTime \
     FULL JOIN deltabase.evrg_30min_delta ON aapl_30min_delta.AAPL_dateTime = EVRG_dateTime \
     FULL JOIN deltabase.ew_30min_delta ON aapl_30min_delta.AAPL_dateTime = EW_dateTime \
     FULL JOIN deltabase.exc_30min_delta ON aapl_30min_delta.AAPL_dateTime = EXC_dateTime \
     FULL JOIN deltabase.expd_30min_delta ON aapl_30min_delta.AAPL_dateTime = EXPD_dateTime \
     FULL JOIN deltabase.expe_30min_delta ON aapl_30min_delta.AAPL_dateTime = EXPE_dateTime \
     FULL JOIN deltabase.exr_30min_delta ON aapl_30min_delta.AAPL_dateTime = EXR_dateTime \
     FULL JOIN deltabase.f_30min_delta ON aapl_30min_delta.AAPL_dateTime = F_dateTime \
     FULL JOIN deltabase.fang_30min_delta ON aapl_30min_delta.AAPL_dateTime = FANG_dateTime \
     FULL JOIN deltabase.fast_30min_delta ON aapl_30min_delta.AAPL_dateTime = FAST_dateTime \
     FULL JOIN deltabase.fb_30min_delta ON aapl_30min_delta.AAPL_dateTime = FB_dateTime \
     FULL JOIN deltabase.fbhs_30min_delta ON aapl_30min_delta.AAPL_dateTime = FBHS_dateTime \
     FULL JOIN deltabase.fcx_30min_delta ON aapl_30min_delta.AAPL_dateTime = FCX_dateTime \
     FULL JOIN deltabase.fds_30min_delta ON aapl_30min_delta.AAPL_dateTime = FDS_dateTime \
     FULL JOIN deltabase.fdx_30min_delta ON aapl_30min_delta.AAPL_dateTime = FDX_dateTime \
     FULL JOIN deltabase.fe_30min_delta ON aapl_30min_delta.AAPL_dateTime = FE_dateTime \
     FULL JOIN deltabase.ffiv_30min_delta ON aapl_30min_delta.AAPL_dateTime = FFIV_dateTime \
     FULL JOIN deltabase.fhn_30min_delta ON aapl_30min_delta.AAPL_dateTime = FHN_dateTime \
     FULL JOIN deltabase.fis_30min_delta ON aapl_30min_delta.AAPL_dateTime = FIS_dateTime \
     FULL JOIN deltabase.fisv_30min_delta ON aapl_30min_delta.AAPL_dateTime = FISV_dateTime \
     FULL JOIN deltabase.fitb_30min_delta ON aapl_30min_delta.AAPL_dateTime = FITB_dateTime \
     FULL JOIN deltabase.fl_30min_delta ON aapl_30min_delta.AAPL_dateTime = FL_dateTime \
     FULL JOIN deltabase.flex_30min_delta ON aapl_30min_delta.AAPL_dateTime = FLEX_dateTime \
     FULL JOIN deltabase.flr_30min_delta ON aapl_30min_delta.AAPL_dateTime = FLR_dateTime \
     FULL JOIN deltabase.fls_30min_delta ON aapl_30min_delta.AAPL_dateTime = FLS_dateTime \
     FULL JOIN deltabase.flt_30min_delta ON aapl_30min_delta.AAPL_dateTime = FLT_dateTime \
     FULL JOIN deltabase.fmc_30min_delta ON aapl_30min_delta.AAPL_dateTime = FMC_dateTime \
     FULL JOIN deltabase.fosl_30min_delta ON aapl_30min_delta.AAPL_dateTime = FOSL_dateTime \
     FULL JOIN deltabase.fox_30min_delta ON aapl_30min_delta.AAPL_dateTime = FOX_dateTime \
     FULL JOIN deltabase.foxa_30min_delta ON aapl_30min_delta.AAPL_dateTime = FOXA_dateTime \
     FULL JOIN deltabase.fpl_30min_delta ON aapl_30min_delta.AAPL_dateTime = FPL_dateTime \
     FULL JOIN deltabase.frc_30min_delta ON aapl_30min_delta.AAPL_dateTime = FRC_dateTime \
     FULL JOIN deltabase.frt_30min_delta ON aapl_30min_delta.AAPL_dateTime = FRT_dateTime \
     FULL JOIN deltabase.fslr_30min_delta ON aapl_30min_delta.AAPL_dateTime = FSLR_dateTime \
     FULL JOIN deltabase.fti_30min_delta ON aapl_30min_delta.AAPL_dateTime = FTI_dateTime \
     FULL JOIN deltabase.ftnt_30min_delta ON aapl_30min_delta.AAPL_dateTime = FTNT_dateTime \
     FULL JOIN deltabase.ftv_30min_delta ON aapl_30min_delta.AAPL_dateTime = FTV_dateTime \
     FULL JOIN deltabase.gci_30min_delta ON aapl_30min_delta.AAPL_dateTime = GCI_dateTime \
     FULL JOIN deltabase.gd_30min_delta ON aapl_30min_delta.AAPL_dateTime = GD_dateTime \
     FULL JOIN deltabase.ge_30min_delta ON aapl_30min_delta.AAPL_dateTime = GE_dateTime \
     FULL JOIN deltabase.ghc_30min_delta ON aapl_30min_delta.AAPL_dateTime = GHC_dateTime \
     FULL JOIN deltabase.gild_30min_delta ON aapl_30min_delta.AAPL_dateTime = GILD_dateTime \
     FULL JOIN deltabase.gis_30min_delta ON aapl_30min_delta.AAPL_dateTime = GIS_dateTime \
     FULL JOIN deltabase.gl_30min_delta ON aapl_30min_delta.AAPL_dateTime = GL_dateTime \
     FULL JOIN deltabase.glw_30min_delta ON aapl_30min_delta.AAPL_dateTime = GLW_dateTime \
     FULL JOIN deltabase.gm_30min_delta ON aapl_30min_delta.AAPL_dateTime = GM_dateTime \
     FULL JOIN deltabase.gme_30min_delta ON aapl_30min_delta.AAPL_dateTime = GME_dateTime \
     FULL JOIN deltabase.gnrc_30min_delta ON aapl_30min_delta.AAPL_dateTime = GNRC_dateTime \
     FULL JOIN deltabase.gnw_30min_delta ON aapl_30min_delta.AAPL_dateTime = GNW_dateTime \
     FULL JOIN deltabase.goog_30min_delta ON aapl_30min_delta.AAPL_dateTime = GOOG_dateTime \
     FULL JOIN deltabase.googl_30min_delta ON aapl_30min_delta.AAPL_dateTime = GOOGL_dateTime \
     FULL JOIN deltabase.gp_30min_delta ON aapl_30min_delta.AAPL_dateTime = GP_dateTime \
     FULL JOIN deltabase.gpc_30min_delta ON aapl_30min_delta.AAPL_dateTime = GPC_dateTime \
     FULL JOIN deltabase.gpn_30min_delta ON aapl_30min_delta.AAPL_dateTime = GPN_dateTime \
     FULL JOIN deltabase.gps_30min_delta ON aapl_30min_delta.AAPL_dateTime = GPS_dateTime \
     FULL JOIN deltabase.grmn_30min_delta ON aapl_30min_delta.AAPL_dateTime = GRMN_dateTime \
     FULL JOIN deltabase.gs_30min_delta ON aapl_30min_delta.AAPL_dateTime = GS_dateTime \
     FULL JOIN deltabase.gt_30min_delta ON aapl_30min_delta.AAPL_dateTime = GT_dateTime \
     FULL JOIN deltabase.gww_30min_delta ON aapl_30min_delta.AAPL_dateTime = GWW_dateTime \
     FULL JOIN deltabase.hal_30min_delta ON aapl_30min_delta.AAPL_dateTime = HAL_dateTime \
     FULL JOIN deltabase.has_30min_delta ON aapl_30min_delta.AAPL_dateTime = HAS_dateTime \
     FULL JOIN deltabase.hban_30min_delta ON aapl_30min_delta.AAPL_dateTime = HBAN_dateTime \
     FULL JOIN deltabase.hbi_30min_delta ON aapl_30min_delta.AAPL_dateTime = HBI_dateTime \
     FULL JOIN deltabase.hca_30min_delta ON aapl_30min_delta.AAPL_dateTime = HCA_dateTime \
     FULL JOIN deltabase.hd_30min_delta ON aapl_30min_delta.AAPL_dateTime = HD_dateTime \
     FULL JOIN deltabase.hes_30min_delta ON aapl_30min_delta.AAPL_dateTime = HES_dateTime \
     FULL JOIN deltabase.hfc_30min_delta ON aapl_30min_delta.AAPL_dateTime = HFC_dateTime \
     FULL JOIN deltabase.hig_30min_delta ON aapl_30min_delta.AAPL_dateTime = HIG_dateTime \
     FULL JOIN deltabase.hii_30min_delta ON aapl_30min_delta.AAPL_dateTime = HII_dateTime \
     FULL JOIN deltabase.hlt_30min_delta ON aapl_30min_delta.AAPL_dateTime = HLT_dateTime \
     FULL JOIN deltabase.hog_30min_delta ON aapl_30min_delta.AAPL_dateTime = HOG_dateTime \
     FULL JOIN deltabase.holx_30min_delta ON aapl_30min_delta.AAPL_dateTime = HOLX_dateTime \
     FULL JOIN deltabase.hon_30min_delta ON aapl_30min_delta.AAPL_dateTime = HON_dateTime \
     FULL JOIN deltabase.hp_30min_delta ON aapl_30min_delta.AAPL_dateTime = HP_dateTime \
     FULL JOIN deltabase.hpe_30min_delta ON aapl_30min_delta.AAPL_dateTime = HPE_dateTime \
     FULL JOIN deltabase.hpq_30min_delta ON aapl_30min_delta.AAPL_dateTime = HPQ_dateTime \
     FULL JOIN deltabase.hrb_30min_delta ON aapl_30min_delta.AAPL_dateTime = HRB_dateTime \
     FULL JOIN deltabase.hrl_30min_delta ON aapl_30min_delta.AAPL_dateTime = HRL_dateTime \
     FULL JOIN deltabase.hsic_30min_delta ON aapl_30min_delta.AAPL_dateTime = HSIC_dateTime \
     FULL JOIN deltabase.hst_30min_delta ON aapl_30min_delta.AAPL_dateTime = HST_dateTime \
     FULL JOIN deltabase.hsy_30min_delta ON aapl_30min_delta.AAPL_dateTime = HSY_dateTime \
     FULL JOIN deltabase.hum_30min_delta ON aapl_30min_delta.AAPL_dateTime = HUM_dateTime \
     FULL JOIN deltabase.iac_30min_delta ON aapl_30min_delta.AAPL_dateTime = IAC_dateTime \
     FULL JOIN deltabase.ibm_30min_delta ON aapl_30min_delta.AAPL_dateTime = IBM_dateTime \
     FULL JOIN deltabase.ice_30min_delta ON aapl_30min_delta.AAPL_dateTime = ICE_dateTime \
     FULL JOIN deltabase.idxx_30min_delta ON aapl_30min_delta.AAPL_dateTime = IDXX_dateTime \
     FULL JOIN deltabase.iex_30min_delta ON aapl_30min_delta.AAPL_dateTime = IEX_dateTime \
     FULL JOIN deltabase.iff_30min_delta ON aapl_30min_delta.AAPL_dateTime = IFF_dateTime \
     FULL JOIN deltabase.igt_30min_delta ON aapl_30min_delta.AAPL_dateTime = IGT_dateTime \
     FULL JOIN deltabase.ihrt_30min_delta ON aapl_30min_delta.AAPL_dateTime = IHRT_dateTime \
     FULL JOIN deltabase.ilmn_30min_delta ON aapl_30min_delta.AAPL_dateTime = ILMN_dateTime \
     FULL JOIN deltabase.incy_30min_delta ON aapl_30min_delta.AAPL_dateTime = INCY_dateTime \
     FULL JOIN deltabase.info_30min_delta ON aapl_30min_delta.AAPL_dateTime = INFO_dateTime \
     FULL JOIN deltabase.infy_30min_delta ON aapl_30min_delta.AAPL_dateTime = INFY_dateTime \
     FULL JOIN deltabase.intc_30min_delta ON aapl_30min_delta.AAPL_dateTime = INTC_dateTime \
     FULL JOIN deltabase.intu_30min_delta ON aapl_30min_delta.AAPL_dateTime = INTU_dateTime \
     FULL JOIN deltabase.ip_30min_delta ON aapl_30min_delta.AAPL_dateTime = IP_dateTime \
     FULL JOIN deltabase.ipg_30min_delta ON aapl_30min_delta.AAPL_dateTime = IPG_dateTime \
     FULL JOIN deltabase.ipgp_30min_delta ON aapl_30min_delta.AAPL_dateTime = IPGP_dateTime \
     FULL JOIN deltabase.iqv_30min_delta ON aapl_30min_delta.AAPL_dateTime = IQV_dateTime \
     FULL JOIN deltabase.ir_30min_delta ON aapl_30min_delta.AAPL_dateTime = IR_dateTime \
     FULL JOIN deltabase.irm_30min_delta ON aapl_30min_delta.AAPL_dateTime = IRM_dateTime \
     FULL JOIN deltabase.isrg_30min_delta ON aapl_30min_delta.AAPL_dateTime = ISRG_dateTime \
     FULL JOIN deltabase.it_30min_delta ON aapl_30min_delta.AAPL_dateTime = IT_dateTime \
     FULL JOIN deltabase.itt_30min_delta ON aapl_30min_delta.AAPL_dateTime = ITT_dateTime \
     FULL JOIN deltabase.itw_30min_delta ON aapl_30min_delta.AAPL_dateTime = ITW_dateTime \
     FULL JOIN deltabase.ivz_30min_delta ON aapl_30min_delta.AAPL_dateTime = IVZ_dateTime \
     FULL JOIN deltabase.j_30min_delta ON aapl_30min_delta.AAPL_dateTime = J_dateTime \
     FULL JOIN deltabase.jbht_30min_delta ON aapl_30min_delta.AAPL_dateTime = JBHT_dateTime \
     FULL JOIN deltabase.jbl_30min_delta ON aapl_30min_delta.AAPL_dateTime = JBL_dateTime \
     FULL JOIN deltabase.jci_30min_delta ON aapl_30min_delta.AAPL_dateTime = JCI_dateTime \
     FULL JOIN deltabase.jd_30min_delta ON aapl_30min_delta.AAPL_dateTime = JD_dateTime \
     FULL JOIN deltabase.jef_30min_delta ON aapl_30min_delta.AAPL_dateTime = JEF_dateTime \
     FULL JOIN deltabase.jkhy_30min_delta ON aapl_30min_delta.AAPL_dateTime = JKHY_dateTime \
     FULL JOIN deltabase.jnj_30min_delta ON aapl_30min_delta.AAPL_dateTime = JNJ_dateTime \
     FULL JOIN deltabase.jnpr_30min_delta ON aapl_30min_delta.AAPL_dateTime = JNPR_dateTime \
     FULL JOIN deltabase.jp_30min_delta ON aapl_30min_delta.AAPL_dateTime = JP_dateTime \
     FULL JOIN deltabase.jpm_30min_delta ON aapl_30min_delta.AAPL_dateTime = JPM_dateTime \
     FULL JOIN deltabase.jwn_30min_delta ON aapl_30min_delta.AAPL_dateTime = JWN_dateTime \
     FULL JOIN deltabase.k_30min_delta ON aapl_30min_delta.AAPL_dateTime = K_dateTime \
     FULL JOIN deltabase.kbh_30min_delta ON aapl_30min_delta.AAPL_dateTime = KBH_dateTime \
     FULL JOIN deltabase.key_30min_delta ON aapl_30min_delta.AAPL_dateTime = KEY_dateTime \
     FULL JOIN deltabase.keys_30min_delta ON aapl_30min_delta.AAPL_dateTime = KEYS_dateTime \
     FULL JOIN deltabase.khc_30min_delta ON aapl_30min_delta.AAPL_dateTime = KHC_dateTime \
     FULL JOIN deltabase.kim_30min_delta ON aapl_30min_delta.AAPL_dateTime = KIM_dateTime \
     FULL JOIN deltabase.klac_30min_delta ON aapl_30min_delta.AAPL_dateTime = KLAC_dateTime \
     FULL JOIN deltabase.kmb_30min_delta ON aapl_30min_delta.AAPL_dateTime = KMB_dateTime \
     FULL JOIN deltabase.kmi_30min_delta ON aapl_30min_delta.AAPL_dateTime = KMI_dateTime \
     FULL JOIN deltabase.kmx_30min_delta ON aapl_30min_delta.AAPL_dateTime = KMX_dateTime \
     FULL JOIN deltabase.ko_30min_delta ON aapl_30min_delta.AAPL_dateTime = KO_dateTime \
     FULL JOIN deltabase.kodk_30min_delta ON aapl_30min_delta.AAPL_dateTime = KODK_dateTime \
     FULL JOIN deltabase.kr_30min_delta ON aapl_30min_delta.AAPL_dateTime = KR_dateTime \
     FULL JOIN deltabase.kss_30min_delta ON aapl_30min_delta.AAPL_dateTime = KSS_dateTime \
     FULL JOIN deltabase.ksu_30min_delta ON aapl_30min_delta.AAPL_dateTime = KSU_dateTime \
     FULL JOIN deltabase.l_30min_delta ON aapl_30min_delta.AAPL_dateTime = L_dateTime \
     FULL JOIN deltabase.lbtyk_30min_delta ON aapl_30min_delta.AAPL_dateTime = LBTYK_dateTime \
     FULL JOIN deltabase.ldos_30min_delta ON aapl_30min_delta.AAPL_dateTime = LDOS_dateTime \
     FULL JOIN deltabase.leg_30min_delta ON aapl_30min_delta.AAPL_dateTime = LEG_dateTime \
     FULL JOIN deltabase.len_30min_delta ON aapl_30min_delta.AAPL_dateTime = LEN_dateTime \
     FULL JOIN deltabase.lh_30min_delta ON aapl_30min_delta.AAPL_dateTime = LH_dateTime \
     FULL JOIN deltabase.lhx_30min_delta ON aapl_30min_delta.AAPL_dateTime = LHX_dateTime \
     FULL JOIN deltabase.life_30min_delta ON aapl_30min_delta.AAPL_dateTime = LIFE_dateTime \
     FULL JOIN deltabase.lin_30min_delta ON aapl_30min_delta.AAPL_dateTime = LIN_dateTime \
     FULL JOIN deltabase.lkq_30min_delta ON aapl_30min_delta.AAPL_dateTime = LKQ_dateTime \
     FULL JOIN deltabase.lly_30min_delta ON aapl_30min_delta.AAPL_dateTime = LLY_dateTime \
     FULL JOIN deltabase.lmt_30min_delta ON aapl_30min_delta.AAPL_dateTime = LMT_dateTime \
     FULL JOIN deltabase.lnc_30min_delta ON aapl_30min_delta.AAPL_dateTime = LNC_dateTime \
     FULL JOIN deltabase.lnt_30min_delta ON aapl_30min_delta.AAPL_dateTime = LNT_dateTime \
     FULL JOIN deltabase.logi_30min_delta ON aapl_30min_delta.AAPL_dateTime = LOGI_dateTime \
     FULL JOIN deltabase.low_30min_delta ON aapl_30min_delta.AAPL_dateTime = LOW_dateTime \
     FULL JOIN deltabase.lrcx_30min_delta ON aapl_30min_delta.AAPL_dateTime = LRCX_dateTime \
     FULL JOIN deltabase.lsi_30min_delta ON aapl_30min_delta.AAPL_dateTime = LSI_dateTime \
     FULL JOIN deltabase.lu_30min_delta ON aapl_30min_delta.AAPL_dateTime = LU_dateTime \
     FULL JOIN deltabase.lumn_30min_delta ON aapl_30min_delta.AAPL_dateTime = LUMN_dateTime \
     FULL JOIN deltabase.luv_30min_delta ON aapl_30min_delta.AAPL_dateTime = LUV_dateTime \
     FULL JOIN deltabase.lvx_30min_delta ON aapl_30min_delta.AAPL_dateTime = LVS_dateTime \
     FULL JOIN deltabase.lw_30min_delta ON aapl_30min_delta.AAPL_dateTime = LW_dateTime \
     FULL JOIN deltabase.lyb_30min_delta ON aapl_30min_delta.AAPL_dateTime = LYB_dateTime \
     FULL JOIN deltabase.lyv_30min_delta ON aapl_30min_delta.AAPL_dateTime = LYV_dateTime \
     FULL JOIN deltabase.m_30min_delta ON aapl_30min_delta.AAPL_dateTime = M_dateTime \
     FULL JOIN deltabase.ma_30min_delta ON aapl_30min_delta.AAPL_dateTime = MA_dateTime \
     FULL JOIN deltabase.maa_30min_delta ON aapl_30min_delta.AAPL_dateTime = MAA_dateTime \
     FULL JOIN deltabase.mac_30min_delta ON aapl_30min_delta.AAPL_dateTime = MAC_dateTime \
     FULL JOIN deltabase.mar_30min_delta ON aapl_30min_delta.AAPL_dateTime = MAR_dateTime \
     FULL JOIN deltabase.mas_30min_delta ON aapl_30min_delta.AAPL_dateTime = MAS_dateTime \
     FULL JOIN deltabase.mat_30min_delta ON aapl_30min_delta.AAPL_dateTime = MAT_dateTime \
     FULL JOIN deltabase.mbi_30min_delta ON aapl_30min_delta.AAPL_dateTime = MBI_dateTime \
     FULL JOIN deltabase.mcd_30min_delta ON aapl_30min_delta.AAPL_dateTime = MCD_dateTime \
     FULL JOIN deltabase.mchp_30min_delta ON aapl_30min_delta.AAPL_dateTime = MCHP_dateTime \
     FULL JOIN deltabase.mck_30min_delta ON aapl_30min_delta.AAPL_dateTime = MCK_dateTime \
     FULL JOIN deltabase.mco_30min_delta ON aapl_30min_delta.AAPL_dateTime = MCO_dateTime \
     FULL JOIN deltabase.mdlz_30min_delta ON aapl_30min_delta.AAPL_dateTime = MDLZ_dateTime \
     FULL JOIN deltabase.mdp_30min_delta ON aapl_30min_delta.AAPL_dateTime = MDP_dateTime \
     FULL JOIN deltabase.mdt_30min_delta ON aapl_30min_delta.AAPL_dateTime = MDT_dateTime \
     FULL JOIN deltabase.met_30min_delta ON aapl_30min_delta.AAPL_dateTime = MET_dateTime \
     FULL JOIN deltabase.mgm_30min_delta ON aapl_30min_delta.AAPL_dateTime = MGM_dateTime \
     FULL JOIN deltabase.mhk_30min_delta ON aapl_30min_delta.AAPL_dateTime = MHK_dateTime \
     FULL JOIN deltabase.mkc_30min_delta ON aapl_30min_delta.AAPL_dateTime = MKC_dateTime \
     FULL JOIN deltabase.mktx_30min_delta ON aapl_30min_delta.AAPL_dateTime = MKTX_dateTime \
     FULL JOIN deltabase.mlm_30min_delta ON aapl_30min_delta.AAPL_dateTime = MLM_dateTime \
     FULL JOIN deltabase.mmc_30min_delta ON aapl_30min_delta.AAPL_dateTime = MMC_dateTime \
     FULL JOIN deltabase.mmi_30min_delta ON aapl_30min_delta.AAPL_dateTime = MMI_dateTime \
     FULL JOIN deltabase.mmm_30min_delta ON aapl_30min_delta.AAPL_dateTime = MMM_dateTime \
     FULL JOIN deltabase.mnst_30min_delta ON aapl_30min_delta.AAPL_dateTime = MNST_dateTime \
     FULL JOIN deltabase.mo_30min_delta ON aapl_30min_delta.AAPL_dateTime = MO_dateTime \
     FULL JOIN deltabase.moh_30min_delta ON aapl_30min_delta.AAPL_dateTime = MOH_dateTime \
     FULL JOIN deltabase.mos_30min_delta ON aapl_30min_delta.AAPL_dateTime = MOS_dateTime \
     FULL JOIN deltabase.mpc_30min_delta ON aapl_30min_delta.AAPL_dateTime = MPC_dateTime \
     FULL JOIN deltabase.mpwr_30min_delta ON aapl_30min_delta.AAPL_dateTime = MPWR_dateTime \
     FULL JOIN deltabase.mrk_30min_delta ON aapl_30min_delta.AAPL_dateTime = MRK_dateTime \
     FULL JOIN deltabase.mro_30min_delta ON aapl_30min_delta.AAPL_dateTime = MRO_dateTime \
     FULL JOIN deltabase.mrvl_30min_delta ON aapl_30min_delta.AAPL_dateTime = MRVL_dateTime \
     FULL JOIN deltabase.ms_30min_delta ON aapl_30min_delta.AAPL_dateTime = MS_dateTime \
     FULL JOIN deltabase.msci_30min_delta ON aapl_30min_delta.AAPL_dateTime = MSCI_dateTime \
     FULL JOIN deltabase.msft_30min_delta ON aapl_30min_delta.AAPL_dateTime = MSFT_dateTime \
     FULL JOIN deltabase.msi_30min_delta ON aapl_30min_delta.AAPL_dateTime = MSI_dateTime \
     FULL JOIN deltabase.mtb_30min_delta ON aapl_30min_delta.AAPL_dateTime = MTB_dateTime \
     FULL JOIN deltabase.mtch_30min_delta ON aapl_30min_delta.AAPL_dateTime = MTCH_dateTime \
     FULL JOIN deltabase.mtd_30min_delta ON aapl_30min_delta.AAPL_dateTime = MTD_dateTime \
     FULL JOIN deltabase.mtw_30min_delta ON aapl_30min_delta.AAPL_dateTime = MTW_dateTime \
     FULL JOIN deltabase.mu_30min_delta ON aapl_30min_delta.AAPL_dateTime = MU_dateTime \
     FULL JOIN deltabase.mur_30min_delta ON aapl_30min_delta.AAPL_dateTime = MUR_dateTime \
     FULL JOIN deltabase.navi_30min_delta ON aapl_30min_delta.AAPL_dateTime = NAVI_dateTime \
     FULL JOIN deltabase.nbr_30min_delta ON aapl_30min_delta.AAPL_dateTime = NBR_dateTime \
     FULL JOIN deltabase.nclh_30min_delta ON aapl_30min_delta.AAPL_dateTime = NCLH_dateTime \
     FULL JOIN deltabase.ndaq_30min_delta ON aapl_30min_delta.AAPL_dateTime = NDAQ_dateTime \
     FULL JOIN deltabase.ndsn_30min_delta ON aapl_30min_delta.AAPL_dateTime = NDSN_dateTime \
     FULL JOIN deltabase.ne_30min_delta ON aapl_30min_delta.AAPL_dateTime = NE_dateTime \
     FULL JOIN deltabase.nee_30min_delta ON aapl_30min_delta.AAPL_dateTime = NEE_dateTime \
     FULL JOIN deltabase.nem_30min_delta ON aapl_30min_delta.AAPL_dateTime = NEM_dateTime \
     FULL JOIN deltabase.nflx_30min_delta ON aapl_30min_delta.AAPL_dateTime = NFLX_dateTime \
     FULL JOIN deltabase.ni_30min_delta ON aapl_30min_delta.AAPL_dateTime = NI_dateTime \
     FULL JOIN deltabase.nke_30min_delta ON aapl_30min_delta.AAPL_dateTime = NKE_dateTime \
     FULL JOIN deltabase.nktr_30min_delta ON aapl_30min_delta.AAPL_dateTime = NKTR_dateTime \
     FULL JOIN deltabase.nlok_30min_delta ON aapl_30min_delta.AAPL_dateTime = NLOK_dateTime \
     FULL JOIN deltabase.nlsn_30min_delta ON aapl_30min_delta.AAPL_dateTime = NLSN_dateTime \
     FULL JOIN deltabase.noc_30min_delta ON aapl_30min_delta.AAPL_dateTime = NOC_dateTime \
     FULL JOIN deltabase.nov_30min_delta ON aapl_30min_delta.AAPL_dateTime = NOV_dateTime \
     FULL JOIN deltabase.now_30min_delta ON aapl_30min_delta.AAPL_dateTime = NOW_dateTime \
     FULL JOIN deltabase.nrg_30min_delta ON aapl_30min_delta.AAPL_dateTime = NRG_dateTime \
     FULL JOIN deltabase.nsc_30min_delta ON aapl_30min_delta.AAPL_dateTime = NSC_dateTime \
     FULL JOIN deltabase.ntap_30min_delta ON aapl_30min_delta.AAPL_dateTime = NTAP_dateTime \
     FULL JOIN deltabase.ntes_30min_delta ON aapl_30min_delta.AAPL_dateTime = NTES_dateTime \
     FULL JOIN deltabase.ntrs_30min_delta ON aapl_30min_delta.AAPL_dateTime = NTRS_dateTime \
     FULL JOIN deltabase.nue_30min_delta ON aapl_30min_delta.AAPL_dateTime = NUE_dateTime \
     FULL JOIN deltabase.nvda_30min_delta ON aapl_30min_delta.AAPL_dateTime = NVDA_dateTime \
     FULL JOIN deltabase.nvr_30min_delta ON aapl_30min_delta.AAPL_dateTime = NVR_dateTime \
     FULL JOIN deltabase.nwl_30min_delta ON aapl_30min_delta.AAPL_dateTime = NWL_dateTime \
     FULL JOIN deltabase.nws_30min_delta ON aapl_30min_delta.AAPL_dateTime = NWS_dateTime \
     FULL JOIN deltabase.nwsa_30min_delta ON aapl_30min_delta.AAPL_dateTime = NWSA_dateTime \
     FULL JOIN deltabase.nxpi_30min_delta ON aapl_30min_delta.AAPL_dateTime = NXPI_dateTime \
     FULL JOIN deltabase.nyt_30min_delta ON aapl_30min_delta.AAPL_dateTime = NYT_dateTime \
     FULL JOIN deltabase.o_30min_delta ON aapl_30min_delta.AAPL_dateTime = O_dateTime \
     FULL JOIN deltabase.odfl_30min_delta ON aapl_30min_delta.AAPL_dateTime = ODFL_dateTime \
     FULL JOIN deltabase.odp_30min_delta ON aapl_30min_delta.AAPL_dateTime = ODP_dateTime \
     FULL JOIN deltabase.ogn_30min_delta ON aapl_30min_delta.AAPL_dateTime = OGN_dateTime \
     FULL JOIN deltabase.oi_30min_delta ON aapl_30min_delta.AAPL_dateTime = OI_dateTime \
     FULL JOIN deltabase.oke_30min_delta ON aapl_30min_delta.AAPL_dateTime = OKE_dateTime \
     FULL JOIN deltabase.omc_30min_delta ON aapl_30min_delta.AAPL_dateTime = OMC_dateTime \
     FULL JOIN deltabase.one_30min_delta ON aapl_30min_delta.AAPL_dateTime = ONE_dateTime \
     FULL JOIN deltabase.orcl_30min_delta ON aapl_30min_delta.AAPL_dateTime = ORCL_dateTime \
     FULL JOIN deltabase.orly_30min_delta ON aapl_30min_delta.AAPL_dateTime = ORLY_dateTime \
     FULL JOIN deltabase.otis_30min_delta ON aapl_30min_delta.AAPL_dateTime = OTIS_dateTime \
     FULL JOIN deltabase.oxy_30min_delta ON aapl_30min_delta.AAPL_dateTime = OXY_dateTime \
     FULL JOIN deltabase.par_30min_delta ON aapl_30min_delta.AAPL_dateTime = PAR_dateTime \
     FULL JOIN deltabase.payc_30min_delta ON aapl_30min_delta.AAPL_dateTime = PAYC_dateTime \
     FULL JOIN deltabase.payx_30min_delta ON aapl_30min_delta.AAPL_dateTime = PAYX_dateTime \
     FULL JOIN deltabase.pbct_30min_delta ON aapl_30min_delta.AAPL_dateTime = PBCT_dateTime \
     FULL JOIN deltabase.pbi_30min_delta ON aapl_30min_delta.AAPL_dateTime = PBI_dateTime \
     FULL JOIN deltabase.pcar_30min_delta ON aapl_30min_delta.AAPL_dateTime = PCAR_dateTime \
     FULL JOIN deltabase.pcg_30min_delta ON aapl_30min_delta.AAPL_dateTime = PCG_dateTime \
     FULL JOIN deltabase.pdco_30min_delta ON aapl_30min_delta.AAPL_dateTime = PDCO_dateTime \
     FULL JOIN deltabase.peak_30min_delta ON aapl_30min_delta.AAPL_dateTime = PEAK_dateTime \
     FULL JOIN deltabase.peg_30min_delta ON aapl_30min_delta.AAPL_dateTime = PEG_dateTime \
     FULL JOIN deltabase.penn_30min_delta ON aapl_30min_delta.AAPL_dateTime = PENN_dateTime \
     FULL JOIN deltabase.pep_30min_delta ON aapl_30min_delta.AAPL_dateTime = PEP_dateTime \
     FULL JOIN deltabase.pfe_30min_delta ON aapl_30min_delta.AAPL_dateTime = PFE_dateTime \
     FULL JOIN deltabase.pfg_30min_delta ON aapl_30min_delta.AAPL_dateTime = PFG_dateTime \
     FULL JOIN deltabase.pg_30min_delta ON aapl_30min_delta.AAPL_dateTime = PG_dateTime \
     FULL JOIN deltabase.pgr_30min_delta ON aapl_30min_delta.AAPL_dateTime = PGR_dateTime \
     FULL JOIN deltabase.ph_30min_delta ON aapl_30min_delta.AAPL_dateTime = PH_dateTime \
     FULL JOIN deltabase.phm_30min_delta ON aapl_30min_delta.AAPL_dateTime = PHM_dateTime \
     FULL JOIN deltabase.pkg_30min_delta ON aapl_30min_delta.AAPL_dateTime = PKG_dateTime \
     FULL JOIN deltabase.pki_30min_delta ON aapl_30min_delta.AAPL_dateTime = PKI_dateTime \
     FULL JOIN deltabase.pld_30min_delta ON aapl_30min_delta.AAPL_dateTime = PLD_dateTime \
     FULL JOIN deltabase.pll_30min_delta ON aapl_30min_delta.AAPL_dateTime = PLL_dateTime \
     FULL JOIN deltabase.pm_30min_delta ON aapl_30min_delta.AAPL_dateTime = PM_dateTime \
     FULL JOIN deltabase.pnc_30min_delta ON aapl_30min_delta.AAPL_dateTime = PNC_dateTime \
     FULL JOIN deltabase.pnr_30min_delta ON aapl_30min_delta.AAPL_dateTime = PNR_dateTime \
     FULL JOIN deltabase.pnw_30min_delta ON aapl_30min_delta.AAPL_dateTime = PNW_dateTime \
     FULL JOIN deltabase.pool_30min_delta ON aapl_30min_delta.AAPL_dateTime = POOL_dateTime \
     FULL JOIN deltabase.ppg_30min_delta ON aapl_30min_delta.AAPL_dateTime = PPG_dateTime \
     FULL JOIN deltabase.ppl_30min_delta ON aapl_30min_delta.AAPL_dateTime = PPL_dateTime \
     FULL JOIN deltabase.prgo_30min_delta ON aapl_30min_delta.AAPL_dateTime = PRGO_dateTime \
     FULL JOIN deltabase.pri_30min_delta ON aapl_30min_delta.AAPL_dateTime = PRI_dateTime \
     FULL JOIN deltabase.pru_30min_delta ON aapl_30min_delta.AAPL_dateTime = PRU_dateTime \
     FULL JOIN deltabase.psa_30min_delta ON aapl_30min_delta.AAPL_dateTime = PSA_dateTime \
     FULL JOIN deltabase.psx_30min_delta ON aapl_30min_delta.AAPL_dateTime = PSX_dateTime \
     FULL JOIN deltabase.ptc_30min_delta ON aapl_30min_delta.AAPL_dateTime = PTC_dateTime \
     FULL JOIN deltabase.pvh_30min_delta ON aapl_30min_delta.AAPL_dateTime = PVH_dateTime \
     FULL JOIN deltabase.pwr_30min_delta ON aapl_30min_delta.AAPL_dateTime = PWR_dateTime \
     FULL JOIN deltabase.pxd_30min_delta ON aapl_30min_delta.AAPL_dateTime = PXD_dateTime \
     FULL JOIN deltabase.pypl_30min_delta ON aapl_30min_delta.AAPL_dateTime = PYPL_dateTime \
     FULL JOIN deltabase.qcom_30min_delta ON aapl_30min_delta.AAPL_dateTime = QCOM_dateTime \
     FULL JOIN deltabase.qgen_30min_delta ON aapl_30min_delta.AAPL_dateTime = QGEN_dateTime \
     FULL JOIN deltabase.qrvo_30min_delta ON aapl_30min_delta.AAPL_dateTime = QRVO_dateTime \
     ORDER BY aapl_30min_delta.AAPL_dateTime ASC;
")

display(data)

# COMMAND ----------

spark.conf.set("spark.sql.execution.arrow.enabled", "true")

#https://cumsum.wordpress.com/2021/03/05/pandas-attributeerror-function-object-has-no-attribute-xxx/
data_pd = data.na.fill(0).pandas_api()

display(data_pd)

# COMMAND ----------

#Replaces the NULL values with a specified value 0.
data_pd_pct = data_pd.pct_change().fillna(0)

display(data_pd_pct)

# COMMAND ----------

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

train_data = scaler.fit(data_pd_pct)

# COMMAND ----------

# initial cluster count
initial_n = 4
 
# train the model
initial_model = KMeans(n_clusters=initial_n)
 
# fit and predict per-household cluster assignment
init_clusters = initial_model.fit_predict(train_data)

# COMMAND ----------

score = metrics.silhouette_score(X, y_cluster_kmeans)
score

# COMMAND ----------

wcss.append(kmeans.inertia_)