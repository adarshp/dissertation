Prospects for new physics at current and future colliders
=========================================================

# Chapter 1: Introduction
    - Standard model - describes fundamental constituents of matter and their interactions
  - Shortcomings of the standard model
  - How to address them? - New physics theories
  - How to test these theories? - Colliders
  - How to bridge theory and experiment - Phenomenology
  - Difficulties to be overcome - how phenomenology can help constrain theory and discover new physics
  - The role of machine learning

# Chapter 2: The Standard Model
  - QFT basics? (Group theory, etc)  — very brief. This can be combined with next section and directly talking about SM gauge group and particle content. 
  - Particle content
  - Electroweak symmetry breaking
  - Interactions
  - Limits of the standard model

# Chapter 3: Beyond the Standard Model
  - Extending the scalar sector: 2HDMs
      - The 2HDM Lagrangian
          - Type-II 2HDM
      - The mass spectrum
      - Interactions
  - Supersymmetry and the MSSM
      - Motivation
        - Hierarchy problem
        - Stable DM candidate
        - Gauge coupling unification
      - Supersymmetry basics
        - Chiral and gauge supermultiplets
        - Interactions
        - The superpotential
      - The MSSM superpotential
      - SUSY breaking
      - SUSY interactions  — brief here.  No need to goto details.
      - R parity and how it implies a stable DM candidate
      - The MSSM Higgs sector and EWSB  — Do we need the MSSM Higgs sector discuss in detail here? If not (means that if we don’t use it in our project), then you can probably pass this section. 
      - The Neutralino and chargino sectors
  - Split SUSY
      - Motivation: Tightenting constraints on the MSSM
      - Description of salient features of split SUSY
      - The motivation for studying electroweakinos     — do we study split SUSY in our project? 
  - Dark Matter
      - History and candidates
      - Methods of detection
      - Constraints

# Chapter 4: Collider phenomenology
  - Scattering amplitudes  — skip
  - From amplitudes to cross-sections — skip.  assume people know what cross section is. 
  - How do we measure cross-sections? General detector design
  - LHC design
      - General overview
      - ATLAS and CMS experiments (put discussion of detector here).
  - FCC-hh
      - Motivation for a new collider
      - Description
  - Anatomy of a collider analysis
      - Monte Carlo simulations - parton-level events
      - Showering and hadronization
      - Detector simulation/reconstruction
      - Event selection and analysis
  - Explanation of statistical significance, 5 sigma
      - Definitions of probability
      - Probability model for an experiment
      - Counting statistics and particle physics
          - Binomial distribution
          - Poisson distribution
          - Gaussian distribution
      - Marked Poisson model, combining channels
      - Likelihood, maximum likelihood estimators
      - Statistical tests
      - Size and power of a test
      - Neyman-Pearson lemma
      - Origins of 5 sigma
      - Different measures of significance, 
          AMS, validity of S/\sqrt{B}  — No need to goto very detail here.  Just put in the things that we need to understand the result. 

Chapter 5: Machine Learning in particle physics
    - Motivation: 
        - EPP as a very hard classification problem
        - Smaller cross sections for new physics
        - Much larger backgrounds at 100 TeV
        - Complex parameter spaces with complicated correlations
    - Brief history
        - First attempts with neural networks
        - Hesitancy of adoption ('black box' mentality)
        - Resurgence of ML with boosted decision trees
    - Description of Boosted Decision Trees
        - Motivation: Excellent 'out-of-box' performance
        - Simple decision trees
        - Ensembles of trees - boosting with AdaBoost
        - Gradient Boosting
    - Implementing BDT in our analyses
        - Split simulated data into training and test sets 
          - Additional validation set would be preferable, but not implemented by us
        - Tuning the classifier
        - Specifying the decision boundary
        - Misc. Notes
          - Dependence on training data

# Chapter 6: Paper 1
  - Motivation: Additional higgses can open up new decay channels not yet searched for.
  - Background: Review experimental limits
  - Analysis strategy: Single top channel angular correlations
  - Results: Show reach in parameter space, low tan beta region especially well covered

Chapter 7: Paper 2
  - Motivation: split SUSY, DM
  - Background: review theoretical and experimental work done in the area
  - Analysis: Razor variables, Boosted decision trees

Chapter 8: Paper 3
  - Motivation: Similar to paper 2, 100 TeV even better for heavy higgses
  - Background: Review literature for heavy higgses
  - Analysis strategy: boosted decision trees
  - Results: N/A yet

Chapter 9: Conclusion
  - Higgs boson success of the LHC
  - What new physics will a 100 TeV collider reveal?
