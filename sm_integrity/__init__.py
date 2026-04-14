"""NANDA Model Integrity Layer.

A Python library for model integrity and trust in NANDA-compatible
agent registries.
"""

from __future__ import annotations

from sm_integrity._types import (
    AttestationMethod,
    GovernanceTier,
    HashAlgorithm,
    LineageRelation,
    ModelType,
    RiskLevel,
)
from sm_integrity.attestation import (
    Attestation,
    HMACSigner,
    HMACVerifier,
    Signer,
    Verifier,
    canonicalize,
    create_attestation,
    verify_attestation,
)
from sm_integrity.governance import (
    REGULATED_POLICIES,
    STANDARD_POLICIES,
    GovernancePolicy,
    GovernanceReport,
    MaxRiskLevel,
    PolicyResult,
    RequireAttestation,
    RequireBaseModel,
    RequireGovernanceTier,
    RequireRiskLevel,
    RequireWeightsHash,
    check_governance,
)
from sm_integrity.hashing import (
    HashProvider,
    IntegrityResult,
    StdlibHashProvider,
    compute_weights_hash,
    verify_integrity,
    verify_provenance_integrity,
)
from sm_integrity.lineage import (
    LineageNode,
    ModelLineage,
)
from sm_integrity.protocol import (
    IntegrityExtension,
    attach_to_agent_facts,
    extract_from_agent_facts,
)
from sm_integrity.provenance import ModelProvenance

__version__ = "0.2.0"

__all__ = [
    # provenance
    "ModelProvenance",
    # enums
    "AttestationMethod",
    "GovernanceTier",
    "HashAlgorithm",
    "LineageRelation",
    "ModelType",
    "RiskLevel",
    # hashing
    "HashProvider",
    "IntegrityResult",
    "StdlibHashProvider",
    "compute_weights_hash",
    "verify_integrity",
    "verify_provenance_integrity",
    # attestation
    "Attestation",
    "HMACSigner",
    "HMACVerifier",
    "Signer",
    "Verifier",
    "canonicalize",
    "create_attestation",
    "verify_attestation",
    # lineage
    "LineageNode",
    "ModelLineage",
    # governance
    "GovernancePolicy",
    "GovernanceReport",
    "MaxRiskLevel",
    "PolicyResult",
    "RequireAttestation",
    "RequireBaseModel",
    "RequireGovernanceTier",
    "RequireRiskLevel",
    "RequireWeightsHash",
    "REGULATED_POLICIES",
    "STANDARD_POLICIES",
    "check_governance",
    # nanda integration
    "IntegrityExtension",
    "attach_to_agent_facts",
    "extract_from_agent_facts",
]
