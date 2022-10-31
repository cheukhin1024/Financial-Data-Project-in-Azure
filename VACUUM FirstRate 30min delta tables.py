# Databricks notebook source
# MAGIC %sql
# MAGIC use deltabase

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Use this when we need to manually vacuum
# MAGIC set spark.databricks.delta.retentionDurationCheck.enabled = False
# MAGIC 
# MAGIC -- Use this when we don't need to manually vacuum
# MAGIC --set spark.databricks.delta.retentionDurationCheck.enabled = True

# COMMAND ----------

# DBTITLE 1,Vacuum Delta Tables
# MAGIC %sql
# MAGIC --vacuum aap_30min_delta retain 0 hours dry run
# MAGIC 
# MAGIC vacuum aapl_30min_delta
# MAGIC vacuum aa_30min_delta
# MAGIC vacuum aal_30min_delta
# MAGIC vacuum aap_30min_delta
# MAGIC vacuum a_30min_delta
# MAGIC vacuum abbv_30min_delta 
# MAGIC vacuum abc_30min_delta 
# MAGIC vacuum abmd_30min_delta
# MAGIC vacuum abt_30min_delta
# MAGIC vacuum acn_30min_delta 
# MAGIC vacuum acv_30min_delta 
# MAGIC vacuum adbe_30min_delta
# MAGIC vacuum adi_30min_delta 
# MAGIC vacuum adm_30min_delta
# MAGIC vacuum adp_30min_delta
# MAGIC vacuum ads_30min_delta
# MAGIC vacuum adsk_30min_delta
# MAGIC vacuum adt_30min_delta 
# MAGIC vacuum aee_30min_delta 
# MAGIC vacuum aep_30min_delta 
# MAGIC vacuum aes_30min_delta 
# MAGIC vacuum afl_30min_delta 
# MAGIC vacuum aig_30min_delta 
# MAGIC vacuum ainv_30min_delta
# MAGIC vacuum aiv_30min_delta 
# MAGIC vacuum aiz_30min_delta 
# MAGIC vacuum ajg_30min_delta 
# MAGIC vacuum akam_30min_delta 
# MAGIC vacuum alb_30min_delta 
# MAGIC vacuum algn_30min_delta 
# MAGIC vacuum alk_30min_delta
# MAGIC vacuum all_30min_delta
# MAGIC vacuum alle_30min_delta 
# MAGIC vacuum altr_30min_delta 
# MAGIC vacuum amat_30min_delta
# MAGIC vacuum ambc_30min_delta
# MAGIC vacuum amcr_30min_delta 
# MAGIC vacuum amd_30min_delta 
# MAGIC vacuum ame_30min_delta
# MAGIC vacuum amg_30min_delta
# MAGIC vacuum amgn_30min_delta
# MAGIC vacuum amp_30min_delta
# MAGIC vacuum amt_30min_delta 
# MAGIC vacuum amzn_30min_delta 
# MAGIC vacuum an_30min_delta
# MAGIC vacuum anet_30min_delta
# MAGIC vacuum anf_30min_delta
# MAGIC vacuum anss_30min_delta 
# MAGIC vacuum antm_30min_delta
# MAGIC vacuum aon_30min_delta 
# MAGIC vacuum aos_30min_delta 
# MAGIC vacuum apa_30min_delta 
# MAGIC vacuum apd_30min_delta 
# MAGIC vacuum aph_30min_delta 
# MAGIC vacuum aptv_30min_delta 
# MAGIC vacuum are_30min_delta 
# MAGIC vacuum arnc_30min_delta 
# MAGIC vacuum ash_30min_delta 
# MAGIC vacuum aso_30min_delta 
# MAGIC vacuum atge_30min_delta 
# MAGIC vacuum ati_30min_delta 
# MAGIC vacuum ato_30min_delta 
# MAGIC vacuum atvi_30min_delta 
# MAGIC vacuum avb_30min_delta 
# MAGIC vacuum avgo_30min_delta 
# MAGIC vacuum avy_30min_delta 
# MAGIC vacuum awk_30min_delta 
# MAGIC vacuum axp_30min_delta 
# MAGIC vacuum ayi_30min_delta 
# MAGIC vacuum azo_30min_delta 
# MAGIC vacuum ba_30min_delta 
# MAGIC vacuum bac_30min_delta 
# MAGIC vacuum bax_30min_delta 
# MAGIC vacuum bbby_30min_delta
# MAGIC vacuum bby_30min_delta 
# MAGIC vacuum bc_30min_delta 
# MAGIC vacuum bdx_30min_delta 
# MAGIC vacuum ben_30min_delta 
# MAGIC vacuum bfb_30min_delta 
# MAGIC vacuum bidu_30min_delta 
# MAGIC vacuum big_30min_delta
# MAGIC vacuum biib_30min_delta 
# MAGIC vacuum bio_30min_delta 
# MAGIC vacuum bk_30min_delta 
# MAGIC vacuum bkng_30min_delta 
# MAGIC vacuum blk_30min_delta 
# MAGIC vacuum bll_30min_delta 
# MAGIC vacuum bmrn_30min_delta 
# MAGIC vacuum bmy_30min_delta 
# MAGIC vacuum br_30min_delta 
# MAGIC vacuum brkb_30min_delta 
# MAGIC vacuum bro_30min_delta 
# MAGIC vacuum bsx_30min_delta 
# MAGIC vacuum btu_30min_delta 
# MAGIC vacuum bud_30min_delta 
# MAGIC vacuum bwa_30min_delta 
# MAGIC       vacuum bxp_30min_delta 
# MAGIC       vacuum c_30min_delta 
# MAGIC       vacuum cag_30min_delta 
# MAGIC       vacuum cah_30min_delta 
# MAGIC       vacuum car_30min_delta
# MAGIC       vacuum carr_30min_delta 
# MAGIC       vacuum cat_30min_delta 
# MAGIC       vacuum cb_30min_delta 
# MAGIC       vacuum cbh_30min_delta 
# MAGIC       vacuum cboe_30min_delta 
# MAGIC       vacuum cbre_30min_delta
# MAGIC       vacuum cc_30min_delta
# MAGIC       vacuum cci_30min_delta
# MAGIC       vacuum cck_30min_delta
# MAGIC       vacuum ccl_30min_delta 
# MAGIC       vacuum ccu_30min_delta
# MAGIC       vacuum cday_30min_delta 
# MAGIC       vacuum cdns_30min_delta 
# MAGIC       vacuum cdw_30min_delta 
# MAGIC       vacuum ce_30min_delta 
# MAGIC       vacuum cern_30min_delta 
# MAGIC       vacuum cf_30min_delta 
# MAGIC       vacuum cfg_30min_delta 
# MAGIC       vacuum chd_30min_delta 
# MAGIC       vacuum chir_30min_delta 
# MAGIC       vacuum chk_30min_delta 
# MAGIC       vacuum chkp_30min_delta 
# MAGIC       vacuum chrw_30min_delta 
# MAGIC       vacuum chtr_30min_delta
# MAGIC       vacuum ci_30min_delta 
# MAGIC       vacuum cien_30min_delta 
# MAGIC       vacuum cinf_30min_delta 
# MAGIC       vacuum cit_30min_delta 
# MAGIC       vacuum cl_30min_delta 
# MAGIC       vacuum clf_30min_delta 
# MAGIC       vacuum clx_30min_delta 
# MAGIC       vacuum cma_30min_delta 
# MAGIC       vacuum cmcsa_30min_delta 
# MAGIC       vacuum cme_30min_delta 
# MAGIC       vacuum cmg_30min_delta 
# MAGIC       vacuum cmi_30min_delta 
# MAGIC       vacuum cms_30min_delta 
# MAGIC       vacuum cnc_30min_delta 
# MAGIC       vacuum cnp_30min_delta 
# MAGIC       vacuum cnx_30min_delta 
# MAGIC       vacuum cof_30min_delta 
# MAGIC       vacuum coo_30min_delta 
# MAGIC       vacuum coop_30min_delta 
# MAGIC       vacuum cop_30min_delta 
# MAGIC       vacuum cost_30min_delta
# MAGIC       vacuum coty_30min_delta 
# MAGIC       vacuum cpb_30min_delta 
# MAGIC       vacuum cpri_30min_delta
# MAGIC       vacuum cprt_30min_delta
# MAGIC       vacuum cpt_30min_delta
# MAGIC       vacuum crm_30min_delta 
# MAGIC       vacuum csco_30min_delta 
# MAGIC       vacuum csx_30min_delta 
# MAGIC       vacuum ctas_30min_delta 
# MAGIC       vacuum ctlt_30min_delta
# MAGIC       vacuum ctsh_30min_delta
# MAGIC       vacuum ctva_30min_delta 
# MAGIC       vacuum ctxs_30min_delta 
# MAGIC       vacuum cvs_30min_delta
# MAGIC       vacuum cvx_30min_delta 
# MAGIC       vacuum czr_30min_delta 
# MAGIC       vacuum d_30min_delta 
# MAGIC       vacuum dal_30min_delta
# MAGIC       vacuum dan_30min_delta
# MAGIC       vacuum dd_30min_delta 
# MAGIC       vacuum dds_30min_delta 
# MAGIC       vacuum de_30min_delta 
# MAGIC       vacuum dell_30min_delta 
# MAGIC       vacuum dfs_30min_delta
# MAGIC       vacuum dg_30min_delta 
# MAGIC       vacuum dgx_30min_delta 
# MAGIC       vacuum dhi_30min_delta
# MAGIC       vacuum dhr_30min_delta
# MAGIC       vacuum dis_30min_delta 
# MAGIC       vacuum disca_30min_delta 
# MAGIC       vacuum disck_30min_delta 
# MAGIC       vacuum dish_30min_delta 
# MAGIC       vacuum dlr_30min_delta 
# MAGIC       vacuum dltr_30min_delta 
# MAGIC       vacuum dlx_30min_delta
# MAGIC       vacuum dnb_30min_delta 
# MAGIC       vacuum dov_30min_delta
# MAGIC       vacuum dow_30min_delta 
# MAGIC       vacuum dpz_30min_delta
# MAGIC       vacuum dre_30min_delta 
# MAGIC       vacuum dri_30min_delta 
# MAGIC       vacuum dte_30min_delta 
# MAGIC       vacuum duk_30min_delta
# MAGIC       vacuum dva_30min_delta 
# MAGIC       vacuum dvn_30min_delta
# MAGIC       vacuum dxc_30min_delta 
# MAGIC       vacuum dxcm_30min_delta 
# MAGIC       vacuum ea_30min_delta 
# MAGIC       vacuum ebay_30min_delta 
# MAGIC       vacuum ecl_30min_delta 
# MAGIC       vacuum ed_30min_delta 
# MAGIC       vacuum efx_30min_delta
# MAGIC       vacuum eix_30min_delta
# MAGIC       vacuum el_30min_delta 
# MAGIC       vacuum emn_30min_delta
# MAGIC       vacuum emr_30min_delta 
# MAGIC       vacuum endp_30min_delta 
# MAGIC       vacuum enph_30min_delta 
# MAGIC       vacuum eog_30min_delta
# MAGIC       vacuum epam_30min_delta 
# MAGIC       vacuum eq_30min_delta
# MAGIC       vacuum eqix_30min_delta 
# MAGIC       vacuum eqr_30min_delta
# MAGIC       vacuum eqt_30min_delta 
# MAGIC       vacuum es_30min_delta 
# MAGIC       vacuum ess_30min_delta 
# MAGIC       vacuum etn_30min_delta 
# MAGIC       vacuum etr_30min_delta 
# MAGIC       vacuum etsy_30min_delta
# MAGIC       vacuum evrg_30min_delta
# MAGIC       vacuum ew_30min_delta 
# MAGIC       vacuum exc_30min_delta 
# MAGIC       vacuum expd_30min_delta 
# MAGIC       vacuum expe_30min_delta 
# MAGIC       vacuum exr_30min_delta 
# MAGIC       vacuum f_30min_delta 
# MAGIC       vacuum fang_30min_delta 
# MAGIC       vacuum fast_30min_delta
# MAGIC       vacuum fb_30min_delta 
# MAGIC       vacuum fbhs_30min_delta 
# MAGIC       vacuum fcx_30min_delta
# MAGIC       vacuum fds_30min_delta 
# MAGIC       vacuum fdx_30min_delta 
# MAGIC       vacuum fe_30min_delta
# MAGIC       vacuum ffiv_30min_delta
# MAGIC       vacuum fhn_30min_delta 
# MAGIC       vacuum fis_30min_delta 
# MAGIC       vacuum fisv_30min_delta 
# MAGIC       vacuum fitb_30min_delta 
# MAGIC       vacuum fl_30min_delta 
# MAGIC       vacuum flex_30min_delta
# MAGIC       vacuum flr_30min_delta
# MAGIC       vacuum fls_30min_delta 
# MAGIC       vacuum flt_30min_delta 
# MAGIC       vacuum fmc_30min_delta 
# MAGIC       vacuum fosl_30min_delta
# MAGIC       vacuum fox_30min_delta 
# MAGIC       vacuum foxa_30min_delta 
# MAGIC       vacuum fpl_30min_delta 
# MAGIC       vacuum frc_30min_delta
# MAGIC       vacuum frt_30min_delta 
# MAGIC       vacuum fslr_30min_delta
# MAGIC       vacuum fti_30min_delta 
# MAGIC       vacuum ftnt_30min_delta 
# MAGIC       vacuum ftv_30min_delta 
# MAGIC       vacuum gci_30min_delta 
# MAGIC       vacuum gd_30min_delta
# MAGIC       vacuum ge_30min_delta 
# MAGIC       vacuum ghc_30min_delta
# MAGIC       vacuum gild_30min_delta
# MAGIC       vacuum gis_30min_delta 
# MAGIC       vacuum gl_30min_delta 
# MAGIC       vacuum glw_30min_delta 
# MAGIC       vacuum gm_30min_delta 
# MAGIC       vacuum gme_30min_delta 
# MAGIC       vacuum gnrc_30min_delta 
# MAGIC       vacuum gnw_30min_delta 
# MAGIC       vacuum goog_30min_delta 
# MAGIC       vacuum googl_30min_delta 
# MAGIC       vacuum gp_30min_delta 
# MAGIC       vacuum gpc_30min_delta 
# MAGIC       vacuum gpn_30min_delta
# MAGIC       vacuum gps_30min_delta 
# MAGIC       vacuum grmn_30min_delta 
# MAGIC       vacuum gs_30min_delta
# MAGIC       vacuum gt_30min_delta 
# MAGIC       vacuum gww_30min_delta
# MAGIC       vacuum hal_30min_delta 
# MAGIC       vacuum has_30min_delta 
# MAGIC       vacuum hban_30min_delta 
# MAGIC       vacuum hbi_30min_delta 
# MAGIC       vacuum hca_30min_delta 
# MAGIC       vacuum hd_30min_delta 
# MAGIC       vacuum hes_30min_delta 
# MAGIC       vacuum hfc_30min_delta 
# MAGIC       vacuum hig_30min_delta 
# MAGIC       vacuum hii_30min_delta 
# MAGIC       vacuum hlt_30min_delta 
# MAGIC       vacuum hog_30min_delta 
# MAGIC       vacuum holx_30min_delta 
# MAGIC       vacuum hon_30min_delta 
# MAGIC       vacuum hp_30min_delta 
# MAGIC       vacuum hpe_30min_delta
# MAGIC       vacuum hpq_30min_delta 
# MAGIC       vacuum hrb_30min_delta 
# MAGIC       vacuum hrl_30min_delta 
# MAGIC       vacuum hsic_30min_delta 
# MAGIC       vacuum hst_30min_delta 
# MAGIC       vacuum hsy_30min_delta 
# MAGIC       vacuum hum_30min_delta
# MAGIC       vacuum iac_30min_delta 
# MAGIC       vacuum ibm_30min_delta 
# MAGIC       vacuum ice_30min_delta
# MAGIC       vacuum idxx_30min_delta 
# MAGIC       vacuum iex_30min_delta 
# MAGIC       vacuum iff_30min_delta 
# MAGIC       vacuum igt_30min_delta 
# MAGIC       vacuum ihrt_30min_delta 
# MAGIC       vacuum ilmn_30min_delta
# MAGIC       vacuum incy_30min_delta 
# MAGIC       vacuum info_30min_delta 
# MAGIC       vacuum infy_30min_delta
# MAGIC       vacuum intc_30min_delta 
# MAGIC       vacuum intu_30min_delta 
# MAGIC       vacuum ip_30min_delta 
# MAGIC       vacuum ipg_30min_delta
# MAGIC       vacuum ipgp_30min_delta 
# MAGIC       vacuum iqv_30min_delta 
# MAGIC       vacuum ir_30min_delta 
# MAGIC       vacuum irm_30min_delta
# MAGIC       vacuum isrg_30min_delta
# MAGIC       vacuum it_30min_delta 
# MAGIC       vacuum itt_30min_delta 
# MAGIC       vacuum itw_30min_delta 
# MAGIC       vacuum ivz_30min_delta 
# MAGIC       vacuum j_30min_delta 
# MAGIC       vacuum jbht_30min_delta 
# MAGIC       vacuum jbl_30min_delta 
# MAGIC       vacuum jci_30min_delta
# MAGIC       vacuum jd_30min_delta
# MAGIC       vacuum jef_30min_delta 
# MAGIC       vacuum jkhy_30min_delta 
# MAGIC       vacuum jnj_30min_delta 
# MAGIC       vacuum jnpr_30min_delta 
# MAGIC       vacuum jp_30min_delta 
# MAGIC       vacuum jpm_30min_delta 
# MAGIC       vacuum jwn_30min_delta 
# MAGIC       vacuum k_30min_delta
# MAGIC       vacuum kbh_30min_delta 
# MAGIC       vacuum key_30min_delta 
# MAGIC       vacuum keys_30min_delta
# MAGIC       vacuum khc_30min_delta 
# MAGIC       vacuum kim_30min_delta 
# MAGIC       vacuum klac_30min_delta
# MAGIC       vacuum kmb_30min_delta 
# MAGIC       vacuum kmi_30min_delta
# MAGIC       vacuum kmx_30min_delta 
# MAGIC       vacuum ko_30min_delta 
# MAGIC       vacuum kodk_30min_delta 
# MAGIC       vacuum kr_30min_delta 
# MAGIC       vacuum kss_30min_delta 
# MAGIC       vacuum ksu_30min_delta
# MAGIC       vacuum l_30min_delta 
# MAGIC       vacuum lbtyk_30min_delta 
# MAGIC       vacuum ldos_30min_delta 
# MAGIC       vacuum leg_30min_delta 
# MAGIC       vacuum len_30min_delta 
# MAGIC       vacuum lh_30min_delta 
# MAGIC       vacuum lhx_30min_delta 
# MAGIC       vacuum life_30min_delta 
# MAGIC       vacuum lin_30min_delta 
# MAGIC       vacuum lkq_30min_delta 
# MAGIC       vacuum lly_30min_delta 
# MAGIC       vacuum lmt_30min_delta 
# MAGIC       vacuum lnc_30min_delta 
# MAGIC       vacuum lnt_30min_delta 
# MAGIC       vacuum logi_30min_delta 
# MAGIC       vacuum low_30min_delta 
# MAGIC       vacuum lrcx_30min_delta 
# MAGIC       vacuum lsi_30min_delta 
# MAGIC       vacuum lu_30min_delta
# MAGIC       vacuum lumn_30min_delta
# MAGIC       vacuum luv_30min_delta 
# MAGIC       vacuum lvs_30min_delta 
# MAGIC       vacuum lw_30min_delta 
# MAGIC       vacuum lyb_30min_delta 
# MAGIC       vacuum lyv_30min_delta 
# MAGIC       vacuum m_30min_delta 
# MAGIC       vacuum ma_30min_delta 
# MAGIC       vacuum maa_30min_delta
# MAGIC       vacuum mac_30min_delta 
# MAGIC       vacuum mar_30min_delta
# MAGIC       vacuum mas_30min_delta 
# MAGIC       vacuum mat_30min_delta 
# MAGIC       vacuum mbi_30min_delta 
# MAGIC       vacuum mcd_30min_delta 
# MAGIC       vacuum mchp_30min_delta
# MAGIC       vacuum mck_30min_delta
# MAGIC       vacuum mco_30min_delta 
# MAGIC       vacuum mdlz_30min_delta 
# MAGIC       vacuum mdp_30min_delta 
# MAGIC       vacuum mdt_30min_delta 
# MAGIC       vacuum met_30min_delta 
# MAGIC       vacuum mgm_30min_delta 
# MAGIC       vacuum mhk_30min_delta 
# MAGIC       vacuum mkc_30min_delta 
# MAGIC       vacuum mktx_30min_delta 
# MAGIC       vacuum mlm_30min_delta 
# MAGIC       vacuum mmc_30min_delta 
# MAGIC       vacuum mmi_30min_delta 
# MAGIC       vacuum mmm_30min_delta 
# MAGIC       vacuum mnst_30min_delta 
# MAGIC       vacuum mo_30min_delta 
# MAGIC       vacuum moh_30min_delta 
# MAGIC       vacuum mos_30min_delta 
# MAGIC       vacuum mpc_30min_delta 
# MAGIC       vacuum mpwr_30min_delta 
# MAGIC       vacuum mrk_30min_delta 
# MAGIC       vacuum mro_30min_delta 
# MAGIC       vacuum mrvl_30min_delta 
# MAGIC       vacuum ms_30min_delta 
# MAGIC       vacuum msci_30min_delta 
# MAGIC       vacuum msft_30min_delta 
# MAGIC       vacuum msi_30min_delta 
# MAGIC       vacuum mtb_30min_delta 
# MAGIC       vacuum mtch_30min_delta 
# MAGIC       vacuum mtd_30min_delta 
# MAGIC       vacuum mtw_30min_delta 
# MAGIC       vacuum mu_30min_delta 
# MAGIC       vacuum mur_30min_delta 
# MAGIC       vacuum navi_30min_delta 
# MAGIC       vacuum nbr_30min_delta 
# MAGIC       vacuum nclh_30min_delta 
# MAGIC       vacuum ndaq_30min_delta 
# MAGIC       vacuum ndsn_30min_delta 
# MAGIC       vacuum ne_30min_delta 
# MAGIC       vacuum nee_30min_delta 
# MAGIC       vacuum nem_30min_delta 
# MAGIC       vacuum nflx_30min_delta 
# MAGIC       vacuum ni_30min_delta 
# MAGIC       vacuum nke_30min_delta 
# MAGIC       vacuum nktr_30min_delta
# MAGIC       vacuum nlok_30min_delta 
# MAGIC       vacuum nlsn_30min_delta 
# MAGIC       vacuum noc_30min_delta 
# MAGIC       vacuum nov_30min_delta
# MAGIC       vacuum now_30min_delta 
# MAGIC       vacuum nrg_30min_delta 
# MAGIC       vacuum nsc_30min_delta 
# MAGIC       vacuum ntap_30min_delta 
# MAGIC       vacuum ntes_30min_delta 
# MAGIC       vacuum ntrs_30min_delta 
# MAGIC       vacuum nue_30min_delta 
# MAGIC       vacuum nvda_30min_delta
# MAGIC       vacuum nvr_30min_delta 
# MAGIC       vacuum nwl_30min_delta 
# MAGIC       vacuum nws_30min_delta 
# MAGIC       vacuum nwsa_30min_delta 
# MAGIC       vacuum nxpi_30min_delta 
# MAGIC       vacuum nyt_30min_delta 
# MAGIC       vacuum o_30min_delta 
# MAGIC       vacuum odfl_30min_delta 
# MAGIC       vacuum odp_30min_delta 
# MAGIC       vacuum ogn_30min_delta
# MAGIC       vacuum oi_30min_delta 
# MAGIC       vacuum oke_30min_delta
# MAGIC       vacuum omc_30min_delta 
# MAGIC       vacuum one_30min_delta 
# MAGIC       vacuum orcl_30min_delta 
# MAGIC       vacuum orly_30min_delta 
# MAGIC       vacuum otis_30min_delta
# MAGIC       vacuum oxy_30min_delta 
# MAGIC       vacuum par_30min_delta
# MAGIC       vacuum payc_30min_delta 
# MAGIC       vacuum payx_30min_delta
# MAGIC       vacuum pbct_30min_delta 
# MAGIC       vacuum pbi_30min_delta 
# MAGIC       vacuum pcar_30min_delta 
# MAGIC       vacuum pcg_30min_delta 
# MAGIC       vacuum pdco_30min_delta 
# MAGIC       vacuum peak_30min_delta
# MAGIC       vacuum peg_30min_delta 
# MAGIC       vacuum penn_30min_delta 
# MAGIC       vacuum pep_30min_delta 
# MAGIC       vacuum pfe_30min_delta
# MAGIC       vacuum pfg_30min_delta 
# MAGIC       vacuum pg_30min_delta 
# MAGIC       vacuum pgr_30min_delta 
# MAGIC       vacuum ph_30min_delta 
# MAGIC       vacuum phm_30min_delta 
# MAGIC       vacuum pkg_30min_delta 
# MAGIC       vacuum pki_30min_delta 
# MAGIC       vacuum pld_30min_delta
# MAGIC       vacuum pll_30min_delta 
# MAGIC       vacuum pm_30min_delta 
# MAGIC       vacuum pnc_30min_delta 
# MAGIC       vacuum pnr_30min_delta 
# MAGIC       vacuum pnw_30min_delta 
# MAGIC       vacuum pool_30min_delta 
# MAGIC       vacuum ppg_30min_delta
# MAGIC       vacuum ppl_30min_delta 
# MAGIC       vacuum prgo_30min_delta
# MAGIC       vacuum pri_30min_delta 
# MAGIC       vacuum pru_30min_delta 
# MAGIC       vacuum psa_30min_delta 
# MAGIC       vacuum psx_30min_delta 
# MAGIC       vacuum ptc_30min_delta 
# MAGIC       vacuum pvh_30min_delta 
# MAGIC       vacuum pwr_30min_delta 
# MAGIC       vacuum pxd_30min_delta 
# MAGIC       vacuum pypl_30min_delta
# MAGIC       vacuum qcom_30min_delta 
# MAGIC       vacuum qgen_30min_delta 
# MAGIC       vacuum qrvo_30min_delta 
# MAGIC       vacuum r_30min_delta 
# MAGIC       vacuum rcl_30min_delta 
# MAGIC       vacuum re_30min_delta 
# MAGIC       vacuum reg_30min_delta
# MAGIC       vacuum regn_30min_delta 
# MAGIC       vacuum rf_30min_delta
# MAGIC       vacuum rhi_30min_delta 
# MAGIC       vacuum rig_30min_delta
# MAGIC       vacuum rjf_30min_delta 
# MAGIC       vacuum rl_30min_delta 
# MAGIC       vacuum rlgy_30min_delta 
# MAGIC       vacuum rmd_30min_delta
# MAGIC       vacuum rok_30min_delta 
# MAGIC       vacuum rol_30min_delta 
# MAGIC       vacuum rop_30min_delta 
# MAGIC       vacuum rost_30min_delta 
# MAGIC       vacuum rrc_30min_delta 
# MAGIC       vacuum rrd_30min_delta 
# MAGIC       vacuum rsg_30min_delta 
# MAGIC       vacuum rtx_30min_delta 
# MAGIC       vacuum ryaay_30min_delta 
# MAGIC       vacuum s_30min_delta 
# MAGIC       vacuum saic_30min_delta 
# MAGIC       vacuum sanm_30min_delta 
# MAGIC       vacuum sbac_30min_delta 
# MAGIC       vacuum sbny_30min_delta
# MAGIC       vacuum sbux_30min_delta 
# MAGIC       vacuum schw_30min_delta 
# MAGIC       vacuum se_30min_delta 
# MAGIC       vacuum sedg_30min_delta 
# MAGIC       vacuum see_30min_delta 
# MAGIC       vacuum shw_30min_delta 
# MAGIC       vacuum sig_30min_delta 
# MAGIC       vacuum siri_30min_delta 
# MAGIC       vacuum sitc_30min_delta 
# MAGIC       vacuum sivb_30min_delta 
# MAGIC       vacuum sjm_30min_delta  
# MAGIC       vacuum slb_30min_delta 
# MAGIC       vacuum slg_30min_delta 
# MAGIC       vacuum slm_30min_delta 
# MAGIC       vacuum sna_30min_delta 
# MAGIC       vacuum snps_30min_delta 
# MAGIC       vacuum so_30min_delta
# MAGIC       vacuum spg_30min_delta 
# MAGIC       vacuum spgi_30min_delta 
# MAGIC       vacuum srcl_30min_delta 
# MAGIC       vacuum sre_30min_delta 
# MAGIC       vacuum ssp_30min_delta 
# MAGIC       vacuum ste_30min_delta 
# MAGIC       vacuum stt_30min_delta 
# MAGIC       vacuum stx_30min_delta 
# MAGIC       vacuum stz_30min_delta 
# MAGIC       vacuum sun_30min_delta 
# MAGIC       vacuum swk_30min_delta 
# MAGIC       vacuum swks_30min_delta 
# MAGIC       vacuum swn_30min_delta 
# MAGIC       vacuum syf_30min_delta
# MAGIC       vacuum syk_30min_delta 
# MAGIC       vacuum syy_30min_delta 
# MAGIC       vacuum t_30min_delta 
# MAGIC       vacuum tap_30min_delta 
# MAGIC       vacuum tdc_30min_delta 
# MAGIC       vacuum tdg_30min_delta 
# MAGIC       vacuum tdy_30min_delta 
# MAGIC       vacuum tel_30min_delta 
# MAGIC       vacuum ter_30min_delta 
# MAGIC       vacuum teva_30min_delta 
# MAGIC       vacuum tex_30min_delta 
# MAGIC       vacuum tfc_30min_delta 
# MAGIC       vacuum tfx_30min_delta 
# MAGIC       vacuum tgna_30min_delta 
# MAGIC       vacuum tgt_30min_delta 
# MAGIC       vacuum thc_30min_delta 
# MAGIC       vacuum tjx_30min_delta 
# MAGIC       vacuum tmo_30min_delta 
# MAGIC       vacuum tmus_30min_delta 
# MAGIC       vacuum tpr_30min_delta 
# MAGIC       vacuum trip_30min_delta 
# MAGIC       vacuum trmb_30min_delta 
# MAGIC       vacuum trow_30min_delta 
# MAGIC       vacuum trv_30min_delta 
# MAGIC       vacuum tsco_30min_delta 
# MAGIC       vacuum tsla_30min_delta 
# MAGIC       vacuum tsn_30min_delta 
# MAGIC       vacuum ttwo_30min_delta
# MAGIC       vacuum tup_30min_delta 
# MAGIC       vacuum twtr_30min_delta 
# MAGIC       vacuum txn_30min_delta 
# MAGIC       vacuum txt_30min_delta
# MAGIC       vacuum tyl_30min_delta 
# MAGIC       vacuum ua_30min_delta 
# MAGIC       vacuum uaa_30min_delta 
# MAGIC       vacuum ual_30min_delta 
# MAGIC       vacuum ucl_30min_delta 
# MAGIC       vacuum udr_30min_delta 
# MAGIC       vacuum uhs_30min_delta 
# MAGIC       vacuum ulta_30min_delta 
# MAGIC       vacuum unh_30min_delta 
# MAGIC       vacuum unm_30min_delta 
# MAGIC       vacuum unp_30min_delta 
# MAGIC       vacuum upc_30min_delta 
# MAGIC       vacuum ups_30min_delta 
# MAGIC       vacuum urbn_30min_delta
# MAGIC       vacuum uri_30min_delta 
# MAGIC       vacuum usb_30min_delta 
# MAGIC       vacuum v_30min_delta 
# MAGIC       vacuum val_30min_delta
# MAGIC       vacuum vfc_30min_delta 
# MAGIC       vacuum viav_30min_delta
# MAGIC       vacuum vlo_30min_delta 
# MAGIC       vacuum vmc_30min_delta 
# MAGIC       vacuum vno_30min_delta 
# MAGIC       vacuum vnt_30min_delta 
# MAGIC       vacuum vod_30min_delta 
# MAGIC       vacuum vrsk_30min_delta 
# MAGIC       vacuum vrsn_30min_delta 
# MAGIC       vacuum vrts_30min_delta 
# MAGIC       vacuum vrtx_30min_delta 
# MAGIC       vacuum vtr_30min_delta 
# MAGIC       vacuum vtrs_30min_delta 
# MAGIC       vacuum vz_30min_delta 
# MAGIC       vacuum wab_30min_delta 
# MAGIC       vacuum wat_30min_delta 
# MAGIC       vacuum wba_30min_delta 
# MAGIC       vacuum wdc_30min_delta 
# MAGIC       vacuum wec_30min_delta 
# MAGIC       vacuum well_30min_delta 
# MAGIC       vacuum wfc_30min_delta 
# MAGIC       vacuum whr_30min_delta 
# MAGIC       vacuum wltw_30min_delta 
# MAGIC       vacuum wm_30min_delta 
# MAGIC       vacuum wmb_30min_delta 
# MAGIC       vacuum wmt_30min_delta 
# MAGIC       vacuum wor_30min_delta 
# MAGIC       vacuum wrb_30min_delta 
# MAGIC       vacuum wrk_30min_delta 
# MAGIC       vacuum wst_30min_delta 
# MAGIC       vacuum wu_30min_delta 
# MAGIC       vacuum wy_30min_delta 
# MAGIC       vacuum wynn_30min_delta 
# MAGIC       vacuum x_30min_delta 
# MAGIC       vacuum xel_30min_delta 
# MAGIC       vacuum xlnx_30min_delta 
# MAGIC       vacuum xom_30min_delta 
# MAGIC       vacuum xray_30min_delta 
# MAGIC       vacuum xrx_30min_delta 
# MAGIC       vacuum xyl_30min_delta 
# MAGIC       vacuum yum_30min_delta 
# MAGIC       vacuum zbh_30min_delta 
# MAGIC       vacuum zbra_30min_delta 
# MAGIC       vacuum zion_30min_delta 
# MAGIC       vacuum zts_30min_delta

# COMMAND ----------

# MAGIC %sql
# MAGIC vacuum aapl_30min_delta dry run
# MAGIC vacuum aa_30min_delta dry run
# MAGIC vacuum aal_30min_delta dry run
# MAGIC vacuum aap_30min_delta dry run
# MAGIC vacuum a_30min_delta dry run
# MAGIC vacuum abbv_30min_delta dry run
# MAGIC vacuum abc_30min_delta dry run
# MAGIC vacuum abmd_30min_delta dry run
# MAGIC vacuum abt_30min_delta dry run
# MAGIC vacuum acn_30min_delta dry run
# MAGIC vacuum acv_30min_delta dry run
# MAGIC vacuum adbe_30min_delta dry run
# MAGIC vacuum adi_30min_delta dry run
# MAGIC vacuum adm_30min_delta dry run
# MAGIC vacuum adp_30min_delta dry run
# MAGIC vacuum ads_30min_delta dry run
# MAGIC vacuum adsk_30min_delta dry run
# MAGIC vacuum adt_30min_delta dry run
# MAGIC vacuum aee_30min_delta dry run
# MAGIC vacuum aep_30min_delta dry run
# MAGIC vacuum aes_30min_delta dry run
# MAGIC vacuum afl_30min_delta dry run 
# MAGIC vacuum aig_30min_delta dry run
# MAGIC vacuum ainv_30min_delta dry run
# MAGIC vacuum aiv_30min_delta dry run
# MAGIC vacuum aiz_30min_delta dry run
# MAGIC vacuum ajg_30min_delta  dry run
# MAGIC vacuum akam_30min_delta dry run
# MAGIC vacuum alb_30min_delta  dry run
# MAGIC vacuum algn_30min_delta dry run
# MAGIC vacuum alk_30min_delta dry run
# MAGIC vacuum all_30min_delta dry run
# MAGIC vacuum alle_30min_delta dry run
# MAGIC vacuum altr_30min_delta dry run
# MAGIC vacuum amat_30min_delta dry run
# MAGIC vacuum ambc_30min_delta dry run
# MAGIC vacuum amcr_30min_delta dry run
# MAGIC vacuum amd_30min_delta dry run
# MAGIC vacuum ame_30min_delta dry run
# MAGIC vacuum amg_30min_delta dry run
# MAGIC vacuum amgn_30min_delta dry run
# MAGIC vacuum amp_30min_delta dry run
# MAGIC vacuum amt_30min_delta  dry run
# MAGIC vacuum amzn_30min_delta  dry run
# MAGIC vacuum an_30min_delta dry run
# MAGIC vacuum anet_30min_delta dry run
# MAGIC vacuum anf_30min_delta dry run
# MAGIC vacuum anss_30min_delta  dry run
# MAGIC vacuum antm_30min_delta dry run
# MAGIC vacuum aon_30min_delta  dry run
# MAGIC vacuum aos_30min_delta  dry run
# MAGIC vacuum apa_30min_delta  dry run
# MAGIC vacuum apd_30min_delta  dry run
# MAGIC vacuum aph_30min_delta  dry run
# MAGIC vacuum aptv_30min_delta  dry run
# MAGIC vacuum are_30min_delta  dry run
# MAGIC vacuum arnc_30min_delta  dry run
# MAGIC vacuum ash_30min_delta  dry run
# MAGIC vacuum aso_30min_delta  dry run
# MAGIC vacuum atge_30min_delta  dry run
# MAGIC vacuum ati_30min_delta  dry run
# MAGIC vacuum ato_30min_delta  dry run
# MAGIC vacuum atvi_30min_delta  dry run
# MAGIC vacuum avb_30min_delta  dry run
# MAGIC vacuum avgo_30min_delta  dry run
# MAGIC vacuum avy_30min_delta  dry run
# MAGIC vacuum awk_30min_delta  dry run
# MAGIC vacuum axp_30min_delta  dry run
# MAGIC vacuum ayi_30min_delta  dry run
# MAGIC vacuum azo_30min_delta  dry run
# MAGIC vacuum ba_30min_delta  dry run
# MAGIC vacuum bac_30min_delta  dry run
# MAGIC vacuum bax_30min_delta  dry run
# MAGIC vacuum bbby_30min_delta dry run
# MAGIC vacuum bby_30min_delta  dry run
# MAGIC vacuum bc_30min_delta  dry run
# MAGIC vacuum bdx_30min_delta  dry run
# MAGIC vacuum ben_30min_delta  dry run
# MAGIC vacuum bfb_30min_delta  dry run
# MAGIC vacuum bidu_30min_delta  dry run
# MAGIC vacuum big_30min_delta dry run
# MAGIC vacuum biib_30min_delta  dry run
# MAGIC vacuum bio_30min_delta  dry run
# MAGIC vacuum bk_30min_delta  dry run
# MAGIC vacuum bkng_30min_delta  dry run
# MAGIC vacuum blk_30min_delta  dry run
# MAGIC vacuum bll_30min_delta  dry run
# MAGIC vacuum bmrn_30min_delta  dry run
# MAGIC vacuum bmy_30min_delta  dry run
# MAGIC vacuum br_30min_delta  dry run
# MAGIC vacuum brkb_30min_delta  dry run
# MAGIC vacuum bro_30min_delta  dry run
# MAGIC vacuum bsx_30min_delta  dry run
# MAGIC vacuum btu_30min_delta  dry run
# MAGIC vacuum bud_30min_delta  dry run
# MAGIC vacuum bwa_30min_delta  dry run
# MAGIC       vacuum bxp_30min_delta  dry run
# MAGIC       vacuum c_30min_delta  dry run
# MAGIC       vacuum cag_30min_delta  dry run
# MAGIC       vacuum cah_30min_delta  dry run
# MAGIC       vacuum car_30min_delta dry run
# MAGIC       vacuum carr_30min_delta  dry run
# MAGIC       vacuum cat_30min_delta  dry run
# MAGIC       vacuum cb_30min_delta  dry run
# MAGIC       vacuum cbh_30min_delta  dry run
# MAGIC       vacuum cboe_30min_delta  dry run
# MAGIC       vacuum cbre_30min_delta dry run
# MAGIC       vacuum cc_30min_delta dry run
# MAGIC       vacuum cci_30min_delta dry run
# MAGIC       vacuum cck_30min_delta dry run
# MAGIC       vacuum ccl_30min_delta  dry run
# MAGIC       vacuum ccu_30min_delta dry run
# MAGIC       vacuum cday_30min_delta  dry run
# MAGIC       vacuum cdns_30min_delta  dry run
# MAGIC       vacuum cdw_30min_delta  dry run
# MAGIC       vacuum ce_30min_delta  dry run
# MAGIC       vacuum cern_30min_delta  dry run
# MAGIC       vacuum cf_30min_delta  dry run
# MAGIC       vacuum cfg_30min_delta  dry run
# MAGIC       vacuum chd_30min_delta  dry run
# MAGIC       vacuum chir_30min_delta  dry run
# MAGIC       vacuum chk_30min_delta  dry run
# MAGIC       vacuum chkp_30min_delta  dry run
# MAGIC       vacuum chrw_30min_delta  dry run
# MAGIC       vacuum chtr_30min_delta dry run
# MAGIC       vacuum ci_30min_delta  dry run
# MAGIC       vacuum cien_30min_delta  dry run
# MAGIC       vacuum cinf_30min_delta  dry run
# MAGIC       vacuum cit_30min_delta  dry run
# MAGIC       vacuum cl_30min_delta  dry run
# MAGIC       vacuum clf_30min_delta  dry run
# MAGIC       vacuum clx_30min_delta  dry run
# MAGIC       vacuum cma_30min_delta  dry run
# MAGIC       vacuum cmcsa_30min_delta  dry run
# MAGIC       vacuum cme_30min_delta  dry run
# MAGIC       vacuum cmg_30min_delta  dry run
# MAGIC       vacuum cmi_30min_delta  dry run
# MAGIC       vacuum cms_30min_delta  dry run
# MAGIC       vacuum cnc_30min_delta  dry run
# MAGIC       vacuum cnp_30min_delta  dry run
# MAGIC       vacuum cnx_30min_delta  dry run
# MAGIC       vacuum cof_30min_delta  dry run
# MAGIC       vacuum coo_30min_delta  dry run
# MAGIC       vacuum coop_30min_delta  dry run
# MAGIC       vacuum cop_30min_delta  dry run
# MAGIC       vacuum cost_30min_delta dry run
# MAGIC       vacuum coty_30min_delta  dry run
# MAGIC       vacuum cpb_30min_delta  dry run
# MAGIC       vacuum cpri_30min_delta dry run 
# MAGIC       vacuum cprt_30min_delta dry run
# MAGIC       vacuum cpt_30min_delta dry run
# MAGIC       vacuum crm_30min_delta  dry run
# MAGIC       vacuum csco_30min_delta  dry run
# MAGIC       vacuum csx_30min_delta  dry run
# MAGIC       vacuum ctas_30min_delta  dry run
# MAGIC       vacuum ctlt_30min_delta dry run
# MAGIC       vacuum ctsh_30min_delta dry run
# MAGIC       vacuum ctva_30min_delta  dry run
# MAGIC       vacuum ctxs_30min_delta  dry run
# MAGIC       vacuum cvs_30min_delta dry run
# MAGIC       vacuum cvx_30min_delta  dry run
# MAGIC       vacuum czr_30min_delta  dry run
# MAGIC       vacuum d_30min_delta  dry run
# MAGIC       vacuum dal_30min_delta dry run
# MAGIC       vacuum dan_30min_delta dry run
# MAGIC       vacuum dd_30min_delta  dry run
# MAGIC       vacuum dds_30min_delta  dry run
# MAGIC       vacuum de_30min_delta  dry run
# MAGIC       vacuum dell_30min_delta  dry run
# MAGIC       vacuum dfs_30min_delta dry run
# MAGIC       vacuum dg_30min_delta  dry run
# MAGIC       vacuum dgx_30min_delta  dry run
# MAGIC       vacuum dhi_30min_delta dry run
# MAGIC       vacuum dhr_30min_delta dry run
# MAGIC       vacuum dis_30min_delta  dry run
# MAGIC       vacuum disca_30min_delta  dry run
# MAGIC       vacuum disck_30min_delta  dry run
# MAGIC       vacuum dish_30min_delta  dry run
# MAGIC       vacuum dlr_30min_delta  dry run
# MAGIC       vacuum dltr_30min_delta  dry run
# MAGIC       vacuum dlx_30min_delta dry run
# MAGIC       vacuum dnb_30min_delta  dry run
# MAGIC       vacuum dov_30min_delta dry run
# MAGIC       vacuum dow_30min_delta  dry run
# MAGIC       vacuum dpz_30min_delta dry run
# MAGIC       vacuum dre_30min_delta  dry run
# MAGIC       vacuum dri_30min_delta  dry run
# MAGIC       vacuum dte_30min_delta  dry run
# MAGIC       vacuum duk_30min_delta dry run
# MAGIC       vacuum dva_30min_delta  dry run
# MAGIC       vacuum dvn_30min_delta dry run
# MAGIC       vacuum dxc_30min_delta  dry run
# MAGIC       vacuum dxcm_30min_delta  dry run
# MAGIC       vacuum ea_30min_delta  dry run
# MAGIC       vacuum ebay_30min_delta  dry run
# MAGIC       vacuum ecl_30min_delta  dry run
# MAGIC       vacuum ed_30min_delta  dry run
# MAGIC       vacuum efx_30min_delta dry run
# MAGIC       vacuum eix_30min_delta dry run
# MAGIC       vacuum el_30min_delta  dry run
# MAGIC       vacuum emn_30min_delta dry run
# MAGIC       vacuum emr_30min_delta  dry run
# MAGIC       vacuum endp_30min_delta  dry run
# MAGIC       vacuum enph_30min_delta  dry run
# MAGIC       vacuum eog_30min_delta dry run
# MAGIC       vacuum epam_30min_delta  dry run
# MAGIC       vacuum eq_30min_delta dry run
# MAGIC       vacuum eqix_30min_delta  dry run
# MAGIC       vacuum eqr_30min_delta dry run
# MAGIC       vacuum eqt_30min_delta  dry run
# MAGIC       vacuum es_30min_delta  dry run
# MAGIC       vacuum ess_30min_delta  dry run
# MAGIC       vacuum etn_30min_delta  dry run
# MAGIC       vacuum etr_30min_delta  dry run
# MAGIC       vacuum etsy_30min_delta dry run
# MAGIC       vacuum evrg_30min_delta dry run
# MAGIC       vacuum ew_30min_delta  dry run
# MAGIC       vacuum exc_30min_delta  dry run
# MAGIC       vacuum expd_30min_delta  dry run
# MAGIC       vacuum expe_30min_delta  dry run
# MAGIC       vacuum exr_30min_delta  dry run
# MAGIC       vacuum f_30min_delta  dry run
# MAGIC       vacuum fang_30min_delta  dry run
# MAGIC       vacuum fast_30min_delta dry run
# MAGIC       vacuum fb_30min_delta  dry run
# MAGIC       vacuum fbhs_30min_delta  dry run
# MAGIC       vacuum fcx_30min_delta dry run
# MAGIC       vacuum fds_30min_delta  dry run
# MAGIC       vacuum fdx_30min_delta  dry run
# MAGIC       vacuum fe_30min_delta dry run
# MAGIC       vacuum ffiv_30min_delta dry run
# MAGIC       vacuum fhn_30min_delta  dry run
# MAGIC       vacuum fis_30min_delta  dry run
# MAGIC       vacuum fisv_30min_delta  dry run
# MAGIC       vacuum fitb_30min_delta  dry run
# MAGIC       vacuum fl_30min_delta  dry run
# MAGIC       vacuum flex_30min_delta dry run
# MAGIC       vacuum flr_30min_delta dry run
# MAGIC       vacuum fls_30min_delta  dry run
# MAGIC       vacuum flt_30min_delta  dry run
# MAGIC       vacuum fmc_30min_delta  dry run
# MAGIC       vacuum fosl_30min_delta dry run
# MAGIC       vacuum fox_30min_delta  dry run
# MAGIC       vacuum foxa_30min_delta  dry run
# MAGIC       vacuum fpl_30min_delta  dry run
# MAGIC       vacuum frc_30min_delta dry run
# MAGIC       vacuum frt_30min_delta  dry run
# MAGIC       vacuum fslr_30min_delta dry run
# MAGIC       vacuum fti_30min_delta  dry run
# MAGIC       vacuum ftnt_30min_delta  dry run
# MAGIC       vacuum ftv_30min_delta  dry run
# MAGIC       vacuum gci_30min_delta  dry run
# MAGIC       vacuum gd_30min_delta dry run
# MAGIC       vacuum ge_30min_delta  dry run
# MAGIC       vacuum ghc_30min_delta dry run
# MAGIC       vacuum gild_30min_delta dry run
# MAGIC       vacuum gis_30min_delta  dry run
# MAGIC       vacuum gl_30min_delta  dry run
# MAGIC       vacuum glw_30min_delta  dry run
# MAGIC       vacuum gm_30min_delta  dry run
# MAGIC       vacuum gme_30min_delta  dry run
# MAGIC       vacuum gnrc_30min_delta  dry run
# MAGIC       vacuum gnw_30min_delta  dry run
# MAGIC       vacuum goog_30min_delta  dry run
# MAGIC       vacuum googl_30min_delta  dry run
# MAGIC       vacuum gp_30min_delta  dry run
# MAGIC       vacuum gpc_30min_delta  dry run
# MAGIC       vacuum gpn_30min_delta dry run
# MAGIC       vacuum gps_30min_delta  dry run
# MAGIC       vacuum grmn_30min_delta  dry run
# MAGIC       vacuum gs_30min_delta dry run
# MAGIC       vacuum gt_30min_delta  dry run
# MAGIC       vacuum gww_30min_delta dry run
# MAGIC       vacuum hal_30min_delta  dry run
# MAGIC       vacuum has_30min_delta  dry run
# MAGIC       vacuum hban_30min_delta  dry run
# MAGIC       vacuum hbi_30min_delta  dry run
# MAGIC       vacuum hca_30min_delta  dry run
# MAGIC       vacuum hd_30min_delta  dry run
# MAGIC       vacuum hes_30min_delta  dry run
# MAGIC       vacuum hfc_30min_delta  dry run
# MAGIC       vacuum hig_30min_delta  dry run
# MAGIC       vacuum hii_30min_delta  dry run
# MAGIC       vacuum hlt_30min_delta  dry run
# MAGIC       vacuum hog_30min_delta  dry run
# MAGIC       vacuum holx_30min_delta  dry run
# MAGIC       vacuum hon_30min_delta  dry run
# MAGIC       vacuum hp_30min_delta  dry run
# MAGIC       vacuum hpe_30min_delta dry run
# MAGIC       vacuum hpq_30min_delta  dry run
# MAGIC       vacuum hrb_30min_delta  dry run
# MAGIC       vacuum hrl_30min_delta  dry run
# MAGIC       vacuum hsic_30min_delta  dry run
# MAGIC       vacuum hst_30min_delta  dry run
# MAGIC       vacuum hsy_30min_delta  dry run
# MAGIC       vacuum hum_30min_delta dry run
# MAGIC       vacuum iac_30min_delta  dry run
# MAGIC       vacuum ibm_30min_delta  dry run
# MAGIC       vacuum ice_30min_deltav dry run
# MAGIC       vacuum idxx_30min_delta  dry run
# MAGIC       vacuum iex_30min_delta  dry run
# MAGIC       vacuum iff_30min_delta  dry run
# MAGIC       vacuum igt_30min_delta  dry run
# MAGIC       vacuum ihrt_30min_delta  dry run
# MAGIC       vacuum ilmn_30min_delta dry run
# MAGIC       vacuum incy_30min_delta  dry run
# MAGIC       vacuum info_30min_delta  dry run
# MAGIC       vacuum infy_30min_delta dry run
# MAGIC       vacuum intc_30min_delta  dry run
# MAGIC       vacuum intu_30min_delta  dry run
# MAGIC       vacuum ip_30min_delta  dry run
# MAGIC       vacuum ipg_30min_delta dry run
# MAGIC       vacuum ipgp_30min_delta  dry run
# MAGIC       vacuum iqv_30min_delta  dry run
# MAGIC       vacuum ir_30min_delta  dry run
# MAGIC       vacuum irm_30min_delta dry run
# MAGIC       vacuum isrg_30min_delta dry run
# MAGIC       vacuum it_30min_delta  dry run
# MAGIC       vacuum itt_30min_delta  dry run
# MAGIC       vacuum itw_30min_delta  dry run
# MAGIC       vacuum ivz_30min_delta  dry run
# MAGIC       vacuum j_30min_delta  dry run
# MAGIC       vacuum jbht_30min_delta  dry run
# MAGIC       vacuum jbl_30min_delta  dry run
# MAGIC       vacuum jci_30min_delta dry run
# MAGIC       vacuum jd_30min_delta dry run
# MAGIC       vacuum jef_30min_delta  dry run
# MAGIC       vacuum jkhy_30min_delta  dry run
# MAGIC       vacuum jnj_30min_delta  dry run
# MAGIC       vacuum jnpr_30min_delta  dry run
# MAGIC       vacuum jp_30min_delta  dry run
# MAGIC       vacuum jpm_30min_delta  dry run
# MAGIC       vacuum jwn_30min_delta  dry run
# MAGIC       vacuum k_30min_delta dry run
# MAGIC       vacuum kbh_30min_delta  dry run
# MAGIC       vacuum key_30min_delta  dry run
# MAGIC       vacuum keys_30min_delta dry run
# MAGIC       vacuum khc_30min_delta  dry run
# MAGIC       vacuum kim_30min_delta  dry run
# MAGIC       vacuum klac_30min_delta dry run
# MAGIC       vacuum kmb_30min_delta  dry run
# MAGIC       vacuum kmi_30min_delta dry run
# MAGIC       vacuum kmx_30min_delta  dry run
# MAGIC       vacuum ko_30min_delta  dry run
# MAGIC       vacuum kodk_30min_delta  dry run
# MAGIC       vacuum kr_30min_delta  dry run
# MAGIC       vacuum kss_30min_delta  dry run
# MAGIC       vacuum ksu_30min_delta dry run
# MAGIC       vacuum l_30min_delta  dry run
# MAGIC       vacuum lbtyk_30min_delta  dry run
# MAGIC       vacuum ldos_30min_delta  dry run
# MAGIC       vacuum leg_30min_delta  dry run
# MAGIC       vacuum len_30min_delta  dry run
# MAGIC       vacuum lh_30min_delta  dry run
# MAGIC       vacuum lhx_30min_delta  dry run
# MAGIC       vacuum life_30min_delta  dry run
# MAGIC       vacuum lin_30min_delta  dry run
# MAGIC       vacuum lkq_30min_delta  dry run
# MAGIC       vacuum lly_30min_delta  dry run
# MAGIC       vacuum lmt_30min_delta  dry run
# MAGIC       vacuum lnc_30min_delta  dry run
# MAGIC       vacuum lnt_30min_delta  dry run
# MAGIC       vacuum logi_30min_delta  dry run
# MAGIC       vacuum low_30min_delta  dry run
# MAGIC       vacuum lrcx_30min_delta  dry run
# MAGIC       vacuum lsi_30min_delta  dry run
# MAGIC       vacuum lu_30min_delta dry run
# MAGIC       vacuum lumn_30min_delta dry run
# MAGIC       vacuum luv_30min_delta  dry run
# MAGIC       vacuum lvs_30min_delta  dry run
# MAGIC       vacuum lw_30min_delta  dry run
# MAGIC       vacuum lyb_30min_delta  dry run
# MAGIC       vacuum lyv_30min_delta  dry run
# MAGIC       vacuum m_30min_delta  dry run
# MAGIC       vacuum ma_30min_delta  dry run
# MAGIC       vacuum maa_30min_delta dry run
# MAGIC       vacuum mac_30min_delta  dry run
# MAGIC       vacuum mar_30min_delta dry run
# MAGIC       vacuum mas_30min_delta  dry run
# MAGIC       vacuum mat_30min_delta  dry run
# MAGIC       vacuum mbi_30min_delta  dry run
# MAGIC       vacuum mcd_30min_delta  dry run
# MAGIC       vacuum mchp_30min_delta dry run
# MAGIC       vacuum mck_30min_delta dry run
# MAGIC       vacuum mco_30min_delta  dry run
# MAGIC       vacuum mdlz_30min_delta  dry run
# MAGIC       vacuum mdp_30min_delta  dry run
# MAGIC       vacuum mdt_30min_delta  dry run
# MAGIC       vacuum met_30min_delta  dry run
# MAGIC       vacuum mgm_30min_delta  dry run
# MAGIC       vacuum mhk_30min_delta  dry run
# MAGIC       vacuum mkc_30min_delta  dry run
# MAGIC       vacuum mktx_30min_delta  dry run
# MAGIC       vacuum mlm_30min_delta  dry run
# MAGIC       vacuum mmc_30min_delta  dry run
# MAGIC       vacuum mmi_30min_delta  dry run
# MAGIC       vacuum mmm_30min_delta  dry run
# MAGIC       vacuum mnst_30min_delta  dry run
# MAGIC       vacuum mo_30min_delta  dry run
# MAGIC       vacuum moh_30min_delta  dry run
# MAGIC       vacuum mos_30min_delta  dry run
# MAGIC       vacuum mpc_30min_delta  dry run
# MAGIC       vacuum mpwr_30min_delta  dry run
# MAGIC       vacuum mrk_30min_delta  dry run
# MAGIC       vacuum mro_30min_delta  dry run
# MAGIC       vacuum mrvl_30min_delta  dry run
# MAGIC       vacuum ms_30min_delta  dry run
# MAGIC       vacuum msci_30min_delta  dry run
# MAGIC       vacuum msft_30min_delta  dry run
# MAGIC       vacuum msi_30min_delta  dry run
# MAGIC       vacuum mtb_30min_delta  dry run
# MAGIC       vacuum mtch_30min_delta  dry run
# MAGIC       vacuum mtd_30min_delta  dry run
# MAGIC       vacuum mtw_30min_delta  dry run
# MAGIC       vacuum mu_30min_delta  dry run
# MAGIC       vacuum mur_30min_delta  dry run
# MAGIC       vacuum navi_30min_delta  dry run
# MAGIC       vacuum nbr_30min_delta  dry run
# MAGIC       vacuum nclh_30min_delta  dry run
# MAGIC       vacuum ndaq_30min_delta  dry run
# MAGIC       vacuum ndsn_30min_delta  dry run
# MAGIC       vacuum ne_30min_delta  dry run
# MAGIC       vacuum nee_30min_delta  dry run
# MAGIC       vacuum nem_30min_delta  dry run
# MAGIC       vacuum nflx_30min_delta  dry run
# MAGIC       vacuum ni_30min_delta  dry run
# MAGIC       vacuum nke_30min_delta  dry run
# MAGIC       vacuum nktr_30min_delta dry run
# MAGIC       vacuum nlok_30min_delta  dry run
# MAGIC       vacuum nlsn_30min_delta  dry run
# MAGIC       vacuum noc_30min_delta  dry run
# MAGIC       vacuum nov_30min_delta dry run
# MAGIC       vacuum now_30min_delta  dry run
# MAGIC       vacuum nrg_30min_delta  dry run
# MAGIC       vacuum nsc_30min_delta  dry run
# MAGIC       vacuum ntap_30min_delta  dry run
# MAGIC       vacuum ntes_30min_delta  dry run
# MAGIC       vacuum ntrs_30min_delta  dry run
# MAGIC       vacuum nue_30min_delta  dry run
# MAGIC       vacuum nvda_30min_delta dry run
# MAGIC       vacuum nvr_30min_delta  dry run
# MAGIC       vacuum nwl_30min_delta  dry run
# MAGIC       vacuum nws_30min_delta  dry run
# MAGIC       vacuum nwsa_30min_delta  dry run
# MAGIC       vacuum nxpi_30min_delta  dry run
# MAGIC       vacuum nyt_30min_delta  dry run
# MAGIC       vacuum o_30min_delta  dry run
# MAGIC       vacuum odfl_30min_delta  dry run
# MAGIC       vacuum odp_30min_delta  dry run
# MAGIC       vacuum ogn_30min_delta dry run
# MAGIC       vacuum oi_30min_delta  dry run
# MAGIC       vacuum oke_30min_delta dry run
# MAGIC       vacuum omc_30min_delta  dry run
# MAGIC       vacuum one_30min_delta  dry run
# MAGIC       vacuum orcl_30min_delta  dry run
# MAGIC       vacuum orly_30min_delta  dry run
# MAGIC       vacuum otis_30min_delta dry run
# MAGIC       vacuum oxy_30min_delta  dry run
# MAGIC       vacuum par_30min_delta dry run
# MAGIC       vacuum payc_30min_delta  dry run
# MAGIC       vacuum payx_30min_delta dry run
# MAGIC       vacuum pbct_30min_delta  dry run
# MAGIC       vacuum pbi_30min_delta  dry run
# MAGIC       vacuum pcar_30min_delta  dry run
# MAGIC       vacuum pcg_30min_delta  dry run
# MAGIC       vacuum pdco_30min_delta  dry run
# MAGIC       vacuum peak_30min_delta dry run
# MAGIC       vacuum peg_30min_delta  dry run
# MAGIC       vacuum penn_30min_delta  dry run
# MAGIC       vacuum pep_30min_delta  dry run
# MAGIC       vacuum pfe_30min_delta dry run
# MAGIC       vacuum pfg_30min_delta  dry run
# MAGIC       vacuum pg_30min_delta  dry run
# MAGIC       vacuum pgr_30min_delta  dry run
# MAGIC       vacuum ph_30min_delta  dry run
# MAGIC       vacuum phm_30min_delta  dry run
# MAGIC       vacuum pkg_30min_delta  dry run
# MAGIC       vacuum pki_30min_delta  dry run
# MAGIC       vacuum pld_30min_delta dry run
# MAGIC       vacuum pll_30min_delta  dry run
# MAGIC       vacuum pm_30min_delta  dry run
# MAGIC       vacuum pnc_30min_delta  dry run
# MAGIC       vacuum pnr_30min_delta  dry run
# MAGIC       vacuum pnw_30min_delta  dry run
# MAGIC       vacuum pool_30min_delta  dry run
# MAGIC       vacuum ppg_30min_delta dry run
# MAGIC       vacuum ppl_30min_delta  dry run
# MAGIC       vacuum prgo_30min_delta dry run
# MAGIC       vacuum pri_30min_delta  dry run
# MAGIC       vacuum pru_30min_delta  dry run
# MAGIC       vacuum psa_30min_delta  dry run
# MAGIC       vacuum psx_30min_delta  dry run
# MAGIC       vacuum ptc_30min_delta  dry run
# MAGIC       vacuum pvh_30min_delta  dry run
# MAGIC       vacuum pwr_30min_delta  dry run
# MAGIC       vacuum pxd_30min_delta  dry run 
# MAGIC       vacuum pypl_30min_delta dry run
# MAGIC       vacuum qcom_30min_delta  dry run
# MAGIC       vacuum qgen_30min_delta  dry run
# MAGIC       vacuum qrvo_30min_delta  dry run
# MAGIC       vacuum r_30min_delta  dry run
# MAGIC       vacuum rcl_30min_delta  dry run
# MAGIC       vacuum re_30min_delta  dry run
# MAGIC       vacuum reg_30min_delta dry run
# MAGIC       vacuum regn_30min_delta  dry run
# MAGIC       vacuum rf_30min_delta dry run
# MAGIC       vacuum rhi_30min_delta  dry run
# MAGIC       vacuum rig_30min_delta dry run
# MAGIC       vacuum rjf_30min_delta  dry run
# MAGIC       vacuum rl_30min_delta  dry run
# MAGIC       vacuum rlgy_30min_delta  dry run
# MAGIC       vacuum rmd_30min_delta dry run
# MAGIC       vacuum rok_30min_delta  dry run
# MAGIC       vacuum rol_30min_delta  dry run
# MAGIC       vacuum rop_30min_delta  dry run
# MAGIC       vacuum rost_30min_delta  dry run
# MAGIC       vacuum rrc_30min_delta  dry run
# MAGIC       vacuum rrd_30min_delta  dry run
# MAGIC       vacuum rsg_30min_delta  dry run
# MAGIC       vacuum rtx_30min_delta  dry run
# MAGIC       vacuum ryaay_30min_delta  dry run
# MAGIC       vacuum s_30min_delta  dry run
# MAGIC       vacuum saic_30min_delta  dry run
# MAGIC       vacuum sanm_30min_delta  dry run
# MAGIC       vacuum sbac_30min_delta  dry run
# MAGIC       vacuum sbny_30min_delta dry run
# MAGIC       vacuum sbux_30min_delta  dry run
# MAGIC       vacuum schw_30min_delta  dry run
# MAGIC       vacuum se_30min_delta  dry run
# MAGIC       vacuum sedg_30min_delta  dry run
# MAGIC       vacuum see_30min_delta  dry run
# MAGIC       vacuum shw_30min_delta  dry run
# MAGIC       vacuum sig_30min_delta  dry run
# MAGIC       vacuum siri_30min_delta  dry run
# MAGIC       vacuum sitc_30min_delta  dry run
# MAGIC       vacuum sivb_30min_delta  dry run
# MAGIC       vacuum sjm_30min_delta   dry run
# MAGIC       vacuum slb_30min_delta  dry run
# MAGIC       vacuum slg_30min_delta  dry run
# MAGIC       vacuum slm_30min_delta  dry run
# MAGIC       vacuum sna_30min_delta  dry run
# MAGIC       vacuum snps_30min_delta  dry run
# MAGIC       vacuum so_30min_delta dry run
# MAGIC       vacuum spg_30min_delta  dry run
# MAGIC       vacuum spgi_30min_delta  dry run
# MAGIC       vacuum srcl_30min_delta  dry run
# MAGIC       vacuum sre_30min_delta  dry run
# MAGIC       vacuum ssp_30min_delta  dry run
# MAGIC       vacuum ste_30min_delta  dry run
# MAGIC       vacuum stt_30min_delta  dry run
# MAGIC       vacuum stx_30min_delta  dry run
# MAGIC       vacuum stz_30min_delta  dry run
# MAGIC       vacuum sun_30min_delta  dry run
# MAGIC       vacuum swk_30min_delta  dry run
# MAGIC       vacuum swks_30min_delta  dry run
# MAGIC       vacuum swn_30min_delta  dry run
# MAGIC       vacuum syf_30min_delta dry run
# MAGIC       vacuum syk_30min_delta  dry run
# MAGIC       vacuum syy_30min_delta  dry run
# MAGIC       vacuum t_30min_delta  dry run
# MAGIC       vacuum tap_30min_delta  dry run
# MAGIC       vacuum tdc_30min_delta  dry run
# MAGIC       vacuum tdg_30min_delta  dry run
# MAGIC       vacuum tdy_30min_delta  dry run
# MAGIC       vacuum tel_30min_delta  dry run
# MAGIC       vacuum ter_30min_delta  dry run
# MAGIC       vacuum teva_30min_delta  dry run
# MAGIC       vacuum tex_30min_delta  dry run
# MAGIC       vacuum tfc_30min_delta  dry run
# MAGIC       vacuum tfx_30min_delta  dry run
# MAGIC       vacuum tgna_30min_delta  dry run
# MAGIC       vacuum tgt_30min_delta  dry run
# MAGIC       vacuum thc_30min_delta  dry run
# MAGIC       vacuum tjx_30min_delta  dry run
# MAGIC       vacuum tmo_30min_delta  dry run
# MAGIC       vacuum tmus_30min_delta  dry run
# MAGIC       vacuum tpr_30min_delta  dry run
# MAGIC       vacuum trip_30min_delta  dry run
# MAGIC       vacuum trmb_30min_delta  dry run
# MAGIC       vacuum trow_30min_delta  dry run
# MAGIC       vacuum trv_30min_delta  dry run
# MAGIC       vacuum tsco_30min_delta  dry run
# MAGIC       vacuum tsla_30min_delta  dry run
# MAGIC       vacuum tsn_30min_delta  dry run
# MAGIC       vacuum ttwo_30min_delta dry run
# MAGIC       vacuum tup_30min_delta  dry run
# MAGIC       vacuum twtr_30min_delta  dry run
# MAGIC       vacuum txn_30min_delta  dry run
# MAGIC       vacuum txt_30min_delta dry run
# MAGIC       vacuum tyl_30min_delta  dry run
# MAGIC       vacuum ua_30min_delta  dry run
# MAGIC       vacuum uaa_30min_delta  dry run
# MAGIC       vacuum ual_30min_delta  dry run
# MAGIC       vacuum ucl_30min_delta  dry run
# MAGIC       vacuum udr_30min_delta  dry run
# MAGIC       vacuum uhs_30min_delta  dry run
# MAGIC       vacuum ulta_30min_delta  dry run
# MAGIC       vacuum unh_30min_delta  dry run
# MAGIC       vacuum unm_30min_delta  dry run
# MAGIC       vacuum unp_30min_delta  dry run
# MAGIC       vacuum upc_30min_delta  dry run
# MAGIC       vacuum ups_30min_delta  dry run
# MAGIC       vacuum urbn_30min_delta dry run
# MAGIC       vacuum uri_30min_delta  dry run
# MAGIC       vacuum usb_30min_delta  dry run
# MAGIC       vacuum v_30min_delta  dry run
# MAGIC       vacuum val_30min_delta dry run
# MAGIC       vacuum vfc_30min_delta  dry run
# MAGIC       vacuum viav_30min_delta dry run
# MAGIC       vacuum vlo_30min_delta  dry run
# MAGIC       vacuum vmc_30min_delta  dry run
# MAGIC       vacuum vno_30min_delta  dry run
# MAGIC       vacuum vnt_30min_delta  dry run
# MAGIC       vacuum vod_30min_delta  dry run
# MAGIC       vacuum vrsk_30min_delta  dry run
# MAGIC       vacuum vrsn_30min_delta  dry run
# MAGIC       vacuum vrts_30min_delta  dry run
# MAGIC       vacuum vrtx_30min_delta  dry run
# MAGIC       vacuum vtr_30min_delta  dry run
# MAGIC       vacuum vtrs_30min_delta  dry run
# MAGIC       vacuum vz_30min_delta  dry run
# MAGIC       vacuum wab_30min_delta  dry run
# MAGIC       vacuum wat_30min_delta  dry run
# MAGIC       vacuum wba_30min_delta  dry run
# MAGIC       vacuum wdc_30min_delta  dry run
# MAGIC       vacuum wec_30min_delta  dry run
# MAGIC       vacuum well_30min_delta  dry run
# MAGIC       vacuum wfc_30min_delta  dry run
# MAGIC       vacuum whr_30min_delta  dry run
# MAGIC       vacuum wltw_30min_delta  dry run
# MAGIC       vacuum wm_30min_delta  dry run
# MAGIC       vacuum wmb_30min_delta  dry run
# MAGIC       vacuum wmt_30min_delta  dry run
# MAGIC       vacuum wor_30min_delta  dry run
# MAGIC       vacuum wrb_30min_delta  dry run
# MAGIC       vacuum wrk_30min_delta  dry run
# MAGIC       vacuum wst_30min_delta  dry run
# MAGIC       vacuum wu_30min_delta  dry run
# MAGIC       vacuum wy_30min_delta  dry run
# MAGIC       vacuum wynn_30min_delta dry run
# MAGIC       vacuum x_30min_delta dry run
# MAGIC       vacuum xel_30min_delta dry run
# MAGIC       vacuum xlnx_30min_delta dry run
# MAGIC       vacuum xom_30min_delta dry run
# MAGIC       vacuum xray_30min_delta dry run
# MAGIC       vacuum xrx_30min_delta dry run
# MAGIC       vacuum xyl_30min_delta dry run
# MAGIC       vacuum yum_30min_delta dry run
# MAGIC       vacuum zbh_30min_delta dry run
# MAGIC       vacuum zbra_30min_delta dry run
# MAGIC       vacuum zion_30min_delta dry run
# MAGIC       vacuum zts_30min_delta dry run

# COMMAND ----------

# MAGIC %sql
# MAGIC describe history aapl_30min_delta 

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Use this when we need to manually vacuum
# MAGIC --set spark.databricks.delta.retentionDurationCheck.enabled = False
# MAGIC 
# MAGIC -- Use this when we don't need to manually vacuum
# MAGIC set spark.databricks.delta.retentionDurationCheck.enabled = True
