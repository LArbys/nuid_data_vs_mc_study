import ROOT as rt

rfile = rt.TFile("out_valid_netanalysis.root")
net = rfile.Get("net")

hnu = rt.TH1D("hnu","",100,0,1.0)
hcosmic = rt.TH1D("hcosmic","",100,0,1.0)

net.Draw("nuprob>>hnu","label==1")
net.Draw("nuprob>>hcosmic","label==0")

c = rt.TCanvas("c","c",800,600)
c.Draw()
hnu.Draw()
hcosmic.SetLineColor(rt.kBlack)
hcosmic.Draw("same")

c.Update()

raw_input()
