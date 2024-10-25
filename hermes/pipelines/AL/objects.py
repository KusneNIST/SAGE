"""Active Learning pipelines."""

from dataclasses import field
from typing import Optional, Type

from pydantic.dataclasses import dataclass as typesafe_dataclass

import hermes.pipelines.base as base
from hermes.archive import Archiver
from hermes.loopcontrols import Initializer


class _Config:  # pylint: disable=too-few-public-methods
    arbitrary_types_allowed = True
    validate_assignment = True


@typesafe_dataclass(config=_Config)
class AL(base.Pipeline):
    """Metaclass for AL."""

    init_method: Type[Initializer] = None
    archive_method: Type[Archiver] = None
    data_analysis: Type[base.Pipeline] = field(init=False)
    # TODO own data archive that takes/returns dict


@typesafe_dataclass(config=_Config)
class ALClusterClassification(AL):
    """Active Learning ClusterClassification Class."""

    data_analysis: Optional[Type[base.ClusterClassification]] = None


@typesafe_dataclass(config=_Config)
class ALRegression(AL):
    """Active Learning Regression Class."""

    data_analysis: Optional[Type[base.Regression]] = None


@typesafe_dataclass(config=_Config)
class ALCluster(AL):
    """Active Learning Cluster Class."""

    data_analysis: Optional[Type[base.Cluster]] = None


@typesafe_dataclass(config=_Config)
class ALClusterRegression(ALCluster):
    """Active Learning ClusterRegression Class."""

    data_analysis: Optional[Type[base.ClusterRegression]] = None


@typesafe_dataclass(config=_Config)
class ALClassificationRegression(AL):
    """Active Learning ClassificationRegression Class."""

    data_analysis: Optional[Type[base.ClassificationRegression]] = None


@typesafe_dataclass(config=_Config)
class ALClusterClassificationRegression(AL):
    """Active Learning ClusterClassificationRegression Class."""

    data_analysis: Optional[Type[base.ClusterClassificationRegression]] = None
