import FWCore.ParameterSet.Config as cms

from Configuration.Eras.Era_Phase2C9_cff import Phase2C9

process = cms.Process('TICL',Phase2C9)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.Geometry.GeometryExtended2026D49Reco_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.RawToDigi_cff')
process.load('Configuration.StandardSequences.L1Reco_cff')
process.load('Configuration.StandardSequences.Reconstruction_cff')
process.load('Configuration.StandardSequences.RecoSim_cff')
process.load('PhysicsTools.PatAlgos.slimming.metFilterPaths_cff')
process.load('Configuration.StandardSequences.PATMC_cff')
process.load('Configuration.StandardSequences.Validation_cff')
process.load('DQMServices.Core.DQMStoreNonLegacy_cff')
process.load('DQMOffline.Configuration.DQMOfflineMC_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1),
    output = cms.optional.untracked.allowed(cms.int32,cms.PSet)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('file:step3.root'),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(
    FailPath = cms.untracked.vstring(),
    IgnoreCompletely = cms.untracked.vstring(),
    Rethrow = cms.untracked.vstring(),
    SkipEvent = cms.untracked.vstring(),
    allowUnscheduled = cms.obsolete.untracked.bool,
    canDeleteEarly = cms.untracked.vstring(),
    emptyRunLumiMode = cms.obsolete.untracked.string,
    eventSetup = cms.untracked.PSet(
        forceNumberOfConcurrentIOVs = cms.untracked.PSet(
            allowAnyLabel_=cms.required.untracked.uint32
        ),
        numberOfConcurrentIOVs = cms.untracked.uint32(1)
    ),
    fileMode = cms.untracked.string('FULLMERGE'),
    forceEventSetupCacheClearOnNewRun = cms.untracked.bool(False),
    makeTriggerResults = cms.obsolete.untracked.bool,
    numberOfConcurrentLuminosityBlocks = cms.untracked.uint32(1),
    numberOfConcurrentRuns = cms.untracked.uint32(1),
    numberOfStreams = cms.untracked.uint32(0),
    numberOfThreads = cms.untracked.uint32(1),
    printDependencies = cms.untracked.bool(False),
    sizeOfStackForThreadsInKB = cms.optional.untracked.uint32,
    throwIfIllegalParameter = cms.untracked.bool(True),
    wantSummary = cms.untracked.bool(False)
)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('step3 nevts:10'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.FEVTTICLoutput = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM-RECO'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('file:step3ticl.root'),
    outputCommands = cms.untracked.vstring( (
        'drop *', 
        'keep *_HGCalRecHit_*_*', 
        'keep recoCaloClusters_hgcalLayerClusters_*_*', 
        'keep *_hgcalLayerClusters_timeLayerCluster_*', 
        'keep *_hgcalLayerClusters_InitialLayerClustersMask_*',
        'keep *_hgcalMultiClusters_*_*', 
        'keep *_iterHGCalMultiClusters_*_*',
        'keep *_ticlTracksters*_*_*', 
        'keep *_ticlMultiClustersFromTracksters*_*_*', 
        'keep edmHepMCProduct_source_*_*', 
        'keep *_genParticle_*_*', 
        'keep *_generator_*_*', 
        'keep *_mix_MergedCaloTruth_*'
    ) ),
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

#process.RandomNumberGeneratorService.restoreStateLabel=cms.untracked.string("randomEngineStateProducer")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:phase2_realistic_T15', '')

#make several TiCL iterations

process.filteredLayerClustersEM1 = cms.EDProducer("FilteredLayerClustersProducer",
    LayerClusters = cms.InputTag("hgcalLayerClusters"),
    LayerClustersInputMask = cms.InputTag("hgcalLayerClusters","InitialLayerClustersMask"),
    algo_number = cms.int32(8),
    clusterFilter = cms.string('ClusterFilterByAlgoAndSizeAndLayerRange'),
    iteration_label = cms.string('EM1'),
    max_cluster_size = cms.int32(9999),
    max_layerId = cms.int32(30),
    mightGet = cms.optional.untracked.vstring,
    min_cluster_size = cms.int32(1),
    min_layerId = cms.int32(0)
)

process.filteredLayerClustersEM2 = process.filteredLayerClustersEM1.clone()
process.filteredLayerClustersEM2.min_cluster_size = cms.int32(2)
process.filteredLayerClustersEM2.iteration_label = cms.string('EM2')

process.filteredLayerClustersEM3 = process.filteredLayerClustersEM1.clone()
process.filteredLayerClustersEM3.min_cluster_size = cms.int32(3)
process.filteredLayerClustersEM3.iteration_label = cms.string('EM3')

process.ticlTrackstersEM1 = cms.EDProducer(
    "TrackstersProducer",
    algo_verbosity = cms.int32(0),
    detector = cms.string('HGCAL'),
    eid_graph_path = cms.string('RecoHGCal/TICL/data/tf_models/energy_id_v0.pb'),
    eid_input_name = cms.string('input'),
    eid_min_cluster_energy = cms.double(1),
    eid_n_clusters = cms.int32(10),
    eid_n_layers = cms.int32(50),
    eid_output_name_energy = cms.string('output/regressed_energy'),
    eid_output_name_id = cms.string('output/id_probabilities'),
    energy_em_over_total_threshold = cms.double(0.0),
    etaLimitIncreaseWindow = cms.double(2.1),
    filter_on_categories = cms.vint32(0, 1),
    filtered_mask = cms.InputTag("filteredLayerClustersEM1","EM1"),
    itername = cms.string('EM1'),
    layer_clusters = cms.InputTag("hgcalLayerClusters"),
    layer_clusters_hfnose_tiles = cms.InputTag("ticlLayerTileHFNose"),
    layer_clusters_tiles = cms.InputTag("ticlLayerTileProducer"),
    max_delta_time = cms.double(3),
    max_longitudinal_sigmaPCA = cms.double(9999),
    max_missing_layers_in_trackster = cms.int32(9999),
    max_out_in_hops = cms.int32(1),
    mightGet = cms.optional.untracked.vstring,
    min_cos_pointing = cms.double(0.9),
    min_cos_theta = cms.double(0.97),
    maxLayer_cospointing = cms.int32(999),
    maxLayer_costheta = cms.int32(999),
    min_layers_per_trackster = cms.int32(1),
    oneTracksterPerTrackSeed = cms.bool(False),
    original_mask = cms.InputTag("hgcalLayerClusters","InitialLayerClustersMask"),
    out_in_dfs = cms.bool(True),
    pid_threshold = cms.double(-1.0),
    promoteEmptyRegionToTrackster = cms.bool(False),
    root_doublet_max_distance_from_seed_squared = cms.double(9999),
    seeding_regions = cms.InputTag("ticlSeedingGlobal"),
    shower_start_max_layer = cms.int32(9999),
    skip_layers = cms.int32(0),
    time_layerclusters = cms.InputTag("hgcalLayerClusters","timeLayerCluster")
)

process.ticlTrackstersEM2 = process.ticlTrackstersEM1.clone()
process.ticlTrackstersEM2.filtered_mask = cms.InputTag("filteredLayerClustersEM2","EM2")
process.ticlTrackstersEM2.itername = cms.string('EM2')

process.ticlTrackstersEM3 = process.ticlTrackstersEM1.clone()
process.ticlTrackstersEM3.filtered_mask = cms.InputTag("filteredLayerClustersEM3","EM3")
process.ticlTrackstersEM3.itername = cms.string('EM3')

process.ticlTrackstersEM1relax = process.ticlTrackstersEM1.clone()
process.ticlTrackstersEM1relax.maxLayer_cospointing = cms.int32(18)
process.ticlTrackstersEM1relax.maxLayer_costheta = cms.int32(18)
process.ticlTrackstersEM1relax.itername = cms.string('EM1relax')

process.ticlTrackstersEM2relax = process.ticlTrackstersEM2.clone()
process.ticlTrackstersEM2relax.maxLayer_cospointing = cms.int32(18)
process.ticlTrackstersEM2relax.maxLayer_costheta = cms.int32(18)
process.ticlTrackstersEM2relax.itername = cms.string('EM2relax')

process.ticlTrackstersEM3relax = process.ticlTrackstersEM3.clone()
process.ticlTrackstersEM3relax.maxLayer_cospointing = cms.int32(18)
process.ticlTrackstersEM3relax.maxLayer_costheta = cms.int32(18)
process.ticlTrackstersEM3relax.itername = cms.string('EM3relax')

process.filteredLayerClustersEMDef = process.filteredLayerClustersEM.clone()
process.filteredLayerClustersEMDef.LayerClustersInputMask = cms.InputTag("hgcalLayerClusters","InitialLayerClustersMask")
process.filteredLayerClustersEMDef.iteration_label = cms.string('EMDef')

process.ticlTrackstersEMDef = process.ticlTrackstersEM.clone()
process.ticlTrackstersEMDef.filtered_mask = cms.InputTag("filteredLayerClustersEMDef","EMDef")
process.ticlTrackstersEMDef.original_mask = cms.InputTag("hgcalLayerClusters","InitialLayerClustersMask")
process.ticlTrackstersEMDef.itername = cms.string('EMDEF')

process.ticlTrackstersDummy1 = process.ticlTrackstersDummy.clone()
process.ticlTrackstersDummy1.filtered_mask = cms.InputTag("filteredLayerClustersEM1", "EM1")
process.ticlTrackstersDummy1.itername = "DUMMY1"

process.ticlTrackstersDummy2 = process.ticlTrackstersDummy1.clone()
process.ticlTrackstersDummy2.filtered_mask = cms.InputTag("filteredLayerClustersEM2", "EM2")
process.ticlTrackstersDummy2.itername = "DUMMY2"

process.ticlTrackstersDummy3 = process.ticlTrackstersDummy1.clone()
process.ticlTrackstersDummy3.filtered_mask = cms.InputTag("filteredLayerClustersEM3", "EM3")
process.ticlTrackstersDummy3.itername = "DUMMY3"



#relax parameters to find lower pT photons
#process.ticlTrackstersEM.min_cos_pointing = cms.double(0.5)#def 0.9
#process.ticlTrackstersEM.min_cos_theta = cms.double(0.5)#def 0.978
##new parameters
#process.ticlTrackstersEM.energy_em_over_total_threshold = cms.double(0.)
#process.ticlTrackstersEM.max_longitudinal_sigmaPCA = cms.double(9999)
#process.ticlTrackstersEM.max_missing_layers_in_trackster = cms.int32(9999)
#process.ticlTrackstersEM.min_layers_per_trackster = cms.int32(1)
#process.ticlTrackstersEM.shower_start_max_layer = cms.int32(9999)
#process.ticlTrackstersEM.skip_layers = cms.int32(0)
#process.ticlTrackstersEM.maxLayer_cospointing = cms.int32(18)
#process.ticlTrackstersEM.maxLayer_costheta = cms.int32(999)

#cms.Path(
#HGCalUncalibRecHit,HGCalRecHit,hgcalRecHitMapProducer,
#hgcalLayerClusters,hgcalMultiClusters,particleFlowRecHitHGC,particleFlowClusterHGCal,particleFlowClusterHGCalFromMultiCl,
#particleFlowSuperClusterHGCal,particleFlowSuperClusterHGCalFromMultiCl,
#ticlLayerTileProducer,
#ticlSeedingGlobal,filteredLayerClustersDummy,ticlTrackstersDummy,ticlMultiClustersFromTrackstersDummy,
#ticlSeedingTrk,filteredLayerClustersTrkEM,ticlTrackstersTrkEM,ticlMultiClustersFromTrackstersTrkEM,
#ticlSeedingGlobal,filteredLayerClustersEM,ticlTrackstersEM,ticlMultiClustersFromTrackstersEM,
#ticlSeedingTrk,filteredLayerClustersTrk,ticlTrackstersTrk,ticlMultiClustersFromTrackstersTrk,
#ticlSeedingGlobal,filteredLayerClustersHAD,ticlTrackstersHAD,ticlMultiClustersFromTrackstersHAD,
#ticlTrackstersMerge,ticlMultiClustersFromTrackstersMerge)
#pfTICL,hgcalTrackCollection,
#)



process.ticl_step = cms.Path(
    process.ticlLayerTileProducer*
    process.ticlSeedingGlobal*process.filteredLayerClustersEM1*process.ticlTrackstersDummy1*process.ticlTrackstersEM1*process.ticlTrackstersEM1relax*
    process.ticlSeedingGlobal*process.filteredLayerClustersEM2*process.ticlTrackstersDummy2*process.ticlTrackstersEM2*process.ticlTrackstersEM2relax*
    process.ticlSeedingGlobal*process.filteredLayerClustersEM3*process.ticlTrackstersDummy3*process.ticlTrackstersEM3*process.ticlTrackstersEM3relax*
    process.ticlSeedingGlobal*process.filteredLayerClustersEMDef*process.ticlTrackstersEMDef
)

process.FEVTTICLoutput_step = cms.EndPath(process.FEVTTICLoutput)

# Schedule definition
process.schedule = cms.Schedule(process.ticl_step,process.FEVTTICLoutput_step)

# customisation of the process.

# customisation of the process.

# Customisation from command line

#Have logErrorHarvester wait for the same EDProducers to finish as those providing data for the OutputModule
from FWCore.Modules.logErrorHarvester_cff import customiseLogErrorHarvesterUsingOutputCommands
process = customiseLogErrorHarvesterUsingOutputCommands(process)

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
