import FWCore.ParameterSet.Config as cms

from RecoHGCal.TICL.TICLSeedingRegions_cff import ticlSeedingGlobal
from RecoHGCal.TICL.ticlLayerTileProducer_cfi import ticlLayerTileProducer as _ticlLayerTileProducer
from RecoHGCal.TICL.trackstersProducer_cfi import trackstersProducer as _trackstersProducer
from RecoHGCal.TICL.filteredLayerClustersProducer_cfi import filteredLayerClustersProducer as _filteredLayerClustersProducer
from RecoHGCal.TICL.multiClustersFromTrackstersProducer_cfi import multiClustersFromTrackstersProducer as _multiClustersFromTrackstersProducer

# CLUSTER FILTERING/MASKING

filteredLayerClustersDummy = _filteredLayerClustersProducer.clone(
  clusterFilter = "ClusterFilterByAlgoAndSize",
  min_cluster_size = 1, #inclusive
  algo_number = 8,
  iteration_label = "Dummy"
)

# CA - PATTERN RECOGNITION

ticlTrackstersDummy = _trackstersProducer.clone(
  filtered_mask = cms.InputTag("filteredLayerClustersDummy", "Dummy"),
  seeding_regions = "ticlSeedingGlobal",
  filter_on_categories = [0, 1, 2, 3, 4, 5], # filter all
  pid_threshold = -1.0, # -1 means: do not filter
  skip_layers = 0,
  max_missing_layers_in_trackster = 9999,
  min_layers_per_trackster = 1,
  shower_start_max_layer = 9999, #no maximum...
  max_longitudinal_sigmaPCA = 9999, #inclusive
  energy_em_over_total_threshold = 0.0,# inclusive
  min_cos_theta = 0., # Fully inclusive
  min_cos_pointing = 0., # Fully inclusive
  maxLayer_cospointing = 999,
  maxLayer_costheta = 999,
  max_delta_time = -1.,
  algo_verbosity = 0,
  oneTracksterPerTrackSeed = False,
  promoteEmptyRegionToTrackster = False,
  itername = "DUMMY"
)


# MULTICLUSTERS

ticlMultiClustersFromTrackstersDummy = _multiClustersFromTrackstersProducer.clone(
    Tracksters = "ticlTrackstersDummy"
)

ticlDummyStepTask = cms.Task(
    ticlSeedingGlobal
    ,filteredLayerClustersDummy
    ,ticlTrackstersDummy
    ,ticlMultiClustersFromTrackstersDummy)

