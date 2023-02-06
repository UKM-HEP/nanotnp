#include "src/compare_efficiency.C"

void compare_eff()
{
  //
  string quantity = "pt";
  //compare_efficiency(quantity, "Efficiency_Result/" + quantity + "/Efficiency_MC.root", "Efficiency_Result/" + quantity + "/Efficiency_Run2011.root");
  compare_efficiency(quantity, "Efficiency_MC.root", "Efficiency_DATA.root");

}
