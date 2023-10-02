# SciDataFlow Asset for the NYGC high-coverage 1000 Genomes GATK Calls

To retrieve the data in this asset, do the following:

    $ git clone https://github.com/scidataflow-assets/nygc_gatk_1000G_highcov.git
    $ sdf pull --all

Be warned that the total size of all data is 1.33TB.

## Methods

The full details of the High-coverage 1000 Genomes GATK processing can be found
on the [1000 Genomes FTP
site](http://ftp.1000genomes.ebi.ac.uk/vol1/ftp/data_collections/1000G_2504_high_coverage/working/20190425_NYGC_GATK/1000G_README_2019April10_NYGCjointcalls.pdf)
(PDF).

## Citation

Please cite the original creators of this data, [Byrska-Bishop et al.
(2022)](https://www.cell.com/cell/fulltext/S0092-8674(22)00991-6):

       M. Byrska-Bishop, U. S. Evani, X. Zhao, A. O. Basile, H. J. Abel, A. A.
       Regier, A. Corvelo, W. E. Clarke, R. Musunuri, K. Nagulapalli, S. Fairley,
       A. Runnels, L. Winterkorn, E. Lowy, Human Genome Structural Variation
       Consortium, Paul Flicek, S. Germer, H. Brand, I. M. Hall, M. E. Talkowski,
       G. Narzisi, M. C. Zody, High-coverage whole-genome sequencing of the
       expanded 1000 Genomes Project cohort including 602 trios. Cell. 185,
       3426–3440.e19 (2022).

BibTeX:

    @ARTICLE{Byrska-Bishop2022-tn,
      title    = "High-coverage whole-genome sequencing of the expanded 1000
                  Genomes Project cohort including 602 trios",
      author   = "Byrska-Bishop, Marta and Evani, Uday S and Zhao, Xuefang and
                  Basile, Anna O and Abel, Haley J and Regier, Allison A and
                  Corvelo, Andr{\'e} and Clarke, Wayne E and Musunuri, Rajeeva and
                  Nagulapalli, Kshithija and Fairley, Susan and Runnels, Alexi and
                  Winterkorn, Lara and Lowy, Ernesto and {Human Genome Structural
                  Variation Consortium} and {Paul Flicek} and Germer, Soren and
                  Brand, Harrison and Hall, Ira M and Talkowski, Michael E and
                  Narzisi, Giuseppe and Zody, Michael C",
      abstract = "The 1000 Genomes Project (1kGP) is the largest fully open
                  resource of whole-genome sequencing (WGS) data consented for
                  public distribution without access or use restrictions. The
                  final, phase 3 release of the 1kGP included 2,504 unrelated
                  samples from 26 populations and was based primarily on
                  low-coverage WGS. Here, we present a high-coverage 3,202-sample
                  WGS 1kGP resource, which now includes 602 complete trios,
                  sequenced to a depth of 30X using Illumina. We performed
                  single-nucleotide variant (SNV) and short insertion and deletion
                  (INDEL) discovery and generated a comprehensive set of structural
                  variants (SVs) by integrating multiple analytic methods through a
                  machine learning model. We show gains in sensitivity and
                  precision of variant calls compared to phase 3, especially among
                  rare SNVs as well as INDELs and SVs spanning frequency spectrum.
                  We also generated an improved reference imputation panel, making
                  variants discovered here accessible for association studies.",
      journal  = "Cell",
      volume   =  185,
      number   =  18,
      pages    = "3426--3440.e19",
      month    =  sep,
      year     =  2022,
      keywords = "1000 Genomes Project; INDEL; SNV; population genetics; reference
                  imputation panel; structural variation; trio sequencing;
                  whole-genome sequencing",
      language = "en"
    }

## Asset Creation Details

This SciDataFlow Asset was created by mapping the 1000 Genomes manifest to a
SciDataFlow data manifest. This was down programmatically; see
`.scidataflow/Makefile` and `.scidataflow/map_manifest.py` for more details.
Note that the ordinary user will not need to use these scripts; simply use `sdf
pull --all` to retrieve the data.
