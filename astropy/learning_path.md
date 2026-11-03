# Astropy learning path: real questions, real data

Use one or two notebook sessions per stage. Focus on answering a small
astronomical question rather than memorizing APIs.

Astropy handles quantities, coordinates, tables, times, and analysis.
Astroquery retrieves data from services such as CDS SIMBAD and ESA Gaia.

## Starting point

- [Units and constants](01_units.ipynb): quantities, physical calculations,
  constants, and equivalencies.
- [Sky coordinates](02_coordinates.ipynb): coordinate formats and separations.
- [FITS images](fits.ipynb): a starting point for the image exercises below.

## 1. SIMBAD to coordinates

**Question:** How far apart are Vega and Sirius on the sky?

Start with [the guided SIMBAD session](03_simbad.ipynb):

1. Retrieve Vega and Sirius in one query.
2. Inspect identifiers, column names, units, and coordinate references.
3. Construct `SkyCoord` objects from the returned positions.
4. Calculate their angular separation.
5. Compare against manually entered coordinates.
6. Save the table as ECSV, reload it, and verify the round trip.

**Outcome:** A real-data separation calculation and a reusable local table.

**Then try:** Add Betelgeuse and Polaris; transform their positions into
Galactic coordinates and describe what longitude and latitude mean.

## 2. Catalogue tables

**Question:** What kinds of catalogued objects lie near the Pleiades?

Query a small region around the Pleiades using SIMBAD. Inspect units,
identifiers, missing values, and query row limits before filtering or sorting.
Learn `Table`, `QTable`, masked columns, and ECSV.

**Outcome:** A saved, filtered catalogue with the service, query, retrieval
date, and selection criteria recorded.

**Caution:** A SIMBAD region query lists identified objects; it is not a
complete, uniformly selected census or a cluster-membership list.

## 3. Plan an observation

**Question:** When are my targets well placed from a chosen observing site?

Use `Time`, `EarthLocation`, and `AltAz` to calculate target altitude through
one night. Include the Sun's altitude, a chosen minimum target altitude, and
an explicit observing date and location.

**Outcome:** An altitude-versus-time plot with nighttime marked.

**Caution:** Label UTC and local time correctly. Explain any IERS data download
warnings, and distinguish geometric altitude from refraction-corrected altitude.

## 4. Explore Gaia stars

**Question:** Which stars near the Pleiades have similar motion and distance?

Query ESA Gaia DR3 around the cluster using a small cone search and basic ADQL.
Inspect proper motions, parallaxes, uncertainties, and catalogue quality fields.
Use explicit row limits and check whether results were truncated.

**Outcome:** A proper-motion diagram showing the cluster concentration and
an explicitly defined candidate selection.

**Caution:** Similar position alone does not establish membership. Record
selection cuts and acknowledge contamination and incompleteness.

## 5. Build a colour-magnitude diagram

**Question:** What stellar sequence do the candidate members trace?

Use Gaia BP/RP colour and G-band photometry. For a beginner distance exercise,
select positive, high signal-to-noise parallaxes, then calculate distances and
absolute magnitudes with units and the distance modulus.

**Outcome:** A colour-magnitude diagram with the magnitude axis inverted.

**Caution:** Do not blindly invert noisy or negative parallaxes. Discuss
extinction, parallax systematics, binaries, and selection effects before
interpreting the diagram. More general distance inference comes later.

## 6. Read a real FITS image

**Question:** How does an astronomical image connect pixels to the sky?

Continue [the existing FITS notebook](fits.ipynb) using the Horsehead Nebula
image in the official Astropy tutorial. Inspect HDUs, header metadata, image
shape, finite pixels, intensity histograms, and display stretches.
Then introduce `WCS` and pixel-to-sky conversion.

**Outcome:** An image with celestial-coordinate axes and a checked
pixel-to-sky-to-pixel round trip.

**Caution:** Image brightness is not automatically calibrated flux.

## 7. Combine image and catalogue data

**Question:** Which catalogued objects can I identify in a survey image?

Obtain a FITS image with valid celestial WCS from a survey archive, such as
MAST, or through Astroquery's SkyView interface. Query the image footprint and
overlay catalogue coordinates using WCS transformations.

**Outcome:** An annotated finding chart with survey provenance, angular scale,
and catalogue identifiers.

**Caution:** Check image and catalogue epochs, proper motion, positional
uncertainties, and matching radius. Nearest does not always mean correct.

## Habits for every session

- Keep units attached until an external API needs plain numbers.
- Inspect returned schemas: current SIMBAD uses lowercase `ra` and `dec`
  with degree-valued coordinates.
- Treat missing measurements explicitly; missing parallax is not zero distance.
- Batch lookups and reuse saved tables instead of repeatedly querying services.
- Record the service or mirror, data release where applicable, query, retrieval
  time, package versions, and selection criteria.
- Do not hide network errors or silently substitute invented data.
- Write a short conclusion: what did you measure, and what are its limitations?

## Official resources

- [Astropy documentation](https://docs.astropy.org/en/stable/)
- [SIMBAD queries with Astroquery](https://astroquery.readthedocs.io/en/stable/simbad/simbad.html)
- [Gaia Archive queries with Astroquery](https://astroquery.readthedocs.io/en/stable/gaia/gaia.html)
- [FITS image tutorial](https://learn.astropy.org/tutorials/FITS-images.html)
- [MAST archive](https://mast.stsci.edu/)

After the introductory SIMBAD session, use **"Which of these stars are
Pleiades members?"** as a first larger project joining stages 2, 4, and 5.
