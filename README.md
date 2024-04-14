# SPECTRA
**S**atellite-powered **P**rediction and **E**valuation of **C**yanobacterial **T**oxicity and **R**isk **A**ssessment
<br/>

We aim to make our efforts in solving the effects of Harmful Algal Blooms (HABS) by creating a predictive Random Forest machine learning model. This model will enable the creation of early warning systems to alert coastal communities, aquaculture industries, and public health agencies about potential HAB events.
<br/>
## Harmful Algal Blooms
- HABs refer to the rapid bloom of certain types of algal species that produce toxins as it reproduces or when it dies <br/>
- They can occur in freshwater, brackish water as well as marine environments, leading to visible discoloration of water.<br/>
- Major types:<br/>
<ins>Biome level toxic HABs</ins> : Produce harmful toxins, posing risks to human health, wildlife, and fisheries.<br/>
<ins>Ichthyic Catastrophes</ins> : Cause massive fish die-offs, through toxin exposure or oxygen depletion or by damaging their gills.<br/>
<ins>Shellfish Contamination</ins> : Contaminate shellfish with toxins, endangering human consumers.<br/>
<ins>Oxygen Depletion</ins> : Decomposition of algal biomass leads to oxygen-depleted dead zones in water.<br/>

There are different classes of HABS including cyanobacteria, dinoflagellate, prymensiophytes, cyptonomads, raphidophytes, diatoms and more. <br/>

According to our in-depth research and analysis we have discovered that about **51% of HABs release toxins**. There are about **2175 animal ilnesses and 117 human illnessses** associated with these toxic releases making it a pressing concern and in need our immediate attention. <br/>

![image](https://github.com/sanjana-vivek/SPECTRA/assets/126575036/6cbaee50-4879-4668-9cb9-8477332331ec) <br/>

<ins>Legend </ins> <br/>
![image](https://github.com/sanjana-vivek/SPECTRA/assets/126575036/7b477635-e719-4df4-9d70-eb779cbbbf39)   Includes the annual reports of documented HAB<br/>
![image](https://github.com/sanjana-vivek/SPECTRA/assets/126575036/42c6fdcf-e3b8-40d8-81a2-9d158ca780ad)   Includes the HAB events that had occcured in a given time period<br/>


## Our solution 
Our idea aims to incorporate machine learning algorithms to predict Harmful Algal Blooms (HABs) in aquatic environments. <br/>
Our project further extends to creating a web interface to send early warning alerts to coastal communities, aquaculture industries and public health agencies about potential HAB events. <br/><br/>
Using **Python** and its machine learning libraries such as Scikit-learn, matlab, pandas this project employs **a predictive Random Forest models** to analyze historical data on environmental conditions, water quality parameters, and past occurrences of HABs and how they depend on geographical and environmental features such as coordinates,  water temperature, chlorophyll a, cells per litre, hpA etc. <br/><br/>
**Satellite imagery data** will be our primary tool in the development of accurate predictive models. Our aim is to integrate space technology to address environmental challenges on Earth. <br/>

### Leveraging satellite data
We have adopted Sentinel 2's Level 2A and MODIS's (Moderate Resolution Imaging Spectroradiometer) imagery for our training and testing dataset. <br/><br/>
**The Sentinel 2** satellite is a European Space Agency (ESA) mission aimed at providing high-resolution optical imagery of Earth's surface for various applications, including environmental monitoring, agriculture, and disaster management.<br/> Launched in 2015, its purpose is to ensure continuity of data from previous satellites and to improve upon their capabilities, offering multispectral imagery with a wide swath width and frequent revisits.<br/> The satellite constellation captures imagery in 13 spectral bands, enabling detailed monitoring of land cover, vegetation health, and changes over time. <br/><br/>
**The Moderate Resolution Imaging Spectroradiometer (MODIS)** satellite was launched by NASA in 1999 aboard the Terra (EOS AM) satellite and in 2002 aboard the Aqua (EOS PM) satellite. It is operated jointly by NASA and the United States Geological Survey (USGS). MODIS captures high-resolution imagery of the Earth's surface in multiple spectral bands, providing valuable data for monitoring changes in the atmosphere, land surface, and oceans for various scientific and environmental applications.

### Our model 
- We have adopted a **Random Forest machine learning model** targeted at detecting the toxicity of the algal bloom as in cells per litre. <br/>
- An algal bloom is classified as a harmful toxic bloom when the toxicity is greater than 15 million cells/litre. <br/>
- Our model has by far the following **accuracy** <br/> <br/>
  ![WhatsApp Image 2024-04-14 at 08 37 11](https://github.com/sanjana-vivek/SPECTRA/assets/126575036/22c6ec62-966f-4bcf-9bee-cdb60ec10a86) <br/>
- Our model **stands apart with this display of the importances of all of it's features** <br/>
  ![Figure_0](https://github.com/sanjana-vivek/SPECTRA/assets/126575036/255562b3-a16b-4fc3-bc08-ceb5864f80bb) <br/>
- The actual data vs predicted data by the model <br/>
![Figure_1](https://github.com/sanjana-vivek/SPECTRA/assets/126575036/392e5d9b-3408-4f48-af77-5e0c3b41114e) <br/>
- Clustered representation <br/>
![Figure_3](https://github.com/sanjana-vivek/SPECTRA/assets/126575036/c10d139c-938b-4354-adcf-deadc55c3b92)

<br/> <br/> 
Our dataset is limited as of now hence there has been a case of over-fitting. 

## Future developments
- Strenghten our model and improve it's accuracy further by enlargening our dataset.
  

