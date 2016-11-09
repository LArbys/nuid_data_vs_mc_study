# UBImageNetTune

This repository contains the files and scripts to train compare the neutrino ID network response for data and MC.

We trained a neutrino ID network by fine tuning GoogLeNet from ImageNet weights. We use the BVLC googlenet model.

Instructions on how this network was trained can be found on the following [wiki pages](https://github.com/LArbys/UBImageNetTune/wiki) that provide brief tutorials on the basics of training and an analysis with the network output.

## Goals

* Compare the neutrino ID scores for EXT-BNB cosmic data and the equivalant EXT-BNB MC events. We want to compare the distribution of data versus MC.
* Compare the mean activations are for data and MC at different layers in the network.  Start with the first and last layers.  Which layers strongly respond to MC or strongly respond to data
* Study the activations of the network to overlay images (EXT-unbiased + MC BNB Neutrino) to those of BNB neutrino open data.  We have a CCQE enriched sample to study.  What layers go off for high/middle/low neutrino score events in data and MC.  Which are common, which are different?
* This will help us prepare to try and train a neutrino ID network where the network is constrained to also reject cosmic MC images in various manners

## Files

| File | purpose |
| ---  | ------- |
| bvlc_googlenet_test.prototxt | network description, in google prototxt format |
| filler_testing.cfg | configuration file for ROOT-caffe interface |
| analyze_test_data.py | example analysis script. for a new analysis, make a copy of this file. try not to overwrite it. |
| setup_env.sh | bash script to setup shell environment.  Will setup the software you need (Caffe, LArCV, ROOT, cuda) | 
| dump_images.py | providing a txt file with list of entries, will output those images if inside ROOT file | 