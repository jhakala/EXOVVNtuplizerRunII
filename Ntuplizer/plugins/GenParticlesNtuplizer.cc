#include "../interface/GenParticlesNtuplizer.h"
 
//===================================================================================================================        
GenParticlesNtuplizer::GenParticlesNtuplizer( std::vector<edm::EDGetTokenT<reco::GenParticleCollection>> tokens, 
					      NtupleBranches* nBranches ) 

   : CandidateNtuplizer( nBranches )
   , genParticlesToken_( tokens[0] )
{

}

//===================================================================================================================        
GenParticlesNtuplizer::~GenParticlesNtuplizer( void )
{
}

//===================================================================================================================        
  void GenParticlesNtuplizer::fillBranches( edm::Event const & event, const edm::EventSetup& iSetup ){
  
    event.getByToken(genParticlesToken_ , genParticles_); 


   /* here we want to save  gen particles info*/
   
    std::vector<int> vDau ;
    std::vector<float> vDauPt ;
    std::vector<float> vDauEta ;
    std::vector<float> vDauPhi ;
    std::vector<float> vDauE ;
    std::vector<int> vMoth;
    std::vector<float> vMothPt ;
    std::vector<float> vMothEta ;
    std::vector<float> vMothPhi ;
    std::vector<float> vMothE ;
    int nMoth = 0;
    int nDau  = 0;  
    for( unsigned p=0; p<genParticles_->size(); ++p ){
      //if( (*genParticles_)[p].status() != 3 ) continue;
      vDau.clear();
      vDauPt.clear();
      vDauEta.clear();
      vDauPhi.clear();
      vDauE.clear();
      vMoth.clear();
      vMothPt.clear();
      vMothEta.clear();
      vMothPhi.clear();
      vMothE.clear();
      nDau = 0; nMoth = 0;
      
      bool isPrompt( (*genParticles_)[p].statusFlags().isPrompt() );
      bool isDirectPromptTauDecayProduct( (*genParticles_)[p].statusFlags().isDirectPromptTauDecayProduct() );
      bool fromHardProcessFinalState( (*genParticles_)[p].fromHardProcessFinalState() );
      bool isDirectHardProcessTauDecayProductFinalState( (*genParticles_)[p].isDirectHardProcessTauDecayProductFinalState() );
      bool isLepton( abs((*genParticles_)[p].pdgId())>=11 && abs((*genParticles_)[p].pdgId())<=18 );
      bool isQuark( abs((*genParticles_)[p].pdgId())<=6 && abs((*genParticles_)[p].status())<=29 );
      bool isPhoton( abs((*genParticles_)[p].pdgId())==22 && (*genParticles_)[p].pt()>10. );
      bool isGluon( abs((*genParticles_)[p].pdgId())==22 && (*genParticles_)[p].pt()>10. );
      bool isWZH( abs((*genParticles_)[p].pdgId())>=23 && abs((*genParticles_)[p].pdgId())<=25 );
      bool isHeavyMeson( abs((*genParticles_)[p].pdgId())>=400 && abs((*genParticles_)[p].pdgId())<=1000 );
      bool isHeavyBaryon( abs((*genParticles_)[p].pdgId())>=4000 && abs((*genParticles_)[p].pdgId())<=10000 );
      bool isBSM( (abs((*genParticles_)[p].pdgId())>=30 && abs((*genParticles_)[p].pdgId())<=50) || abs((*genParticles_)[p].pdgId())>=1000000 );
      
      if(!isLepton && !isQuark && !isPhoton && !isGluon && !isWZH && !isHeavyMeson && !isHeavyBaryon && !isBSM && !isDirectPromptTauDecayProduct && !fromHardProcessFinalState && !isDirectHardProcessTauDecayProductFinalState) continue;
      
      nBranches_->genParticle_pt    .push_back((*genParticles_)[p].pt()     );
      nBranches_->genParticle_eta   .push_back((*genParticles_)[p].eta()    );
      nBranches_->genParticle_phi   .push_back((*genParticles_)[p].phi()    );
      nBranches_->genParticle_mass  .push_back((*genParticles_)[p].mass()   );
      nBranches_->genParticle_status.push_back((*genParticles_)[p].status() );
      nBranches_->genParticle_pdgId .push_back((*genParticles_)[p].pdgId()  );

      for( unsigned int m=0; m<(*genParticles_)[p].numberOfMothers(); m++){
        vMoth.push_back( (*genParticles_)[p].mother(m)->pdgId() );
	vMothPt.push_back( (*genParticles_)[p].mother(m)->pt() );
	vMothEta.push_back( (*genParticles_)[p].mother(m)->eta() );
	vMothPhi.push_back( (*genParticles_)[p].mother(m)->phi() );
	vMothE.push_back( (*genParticles_)[p].mother(m)->energy() );
	nMoth++;
      }

      for( unsigned int d=0; d<(*genParticles_)[p].numberOfDaughters(); d++ ){
        vDau.push_back( (*genParticles_)[p].daughter(d)->pdgId() );
	vDauPt.push_back( (*genParticles_)[p].daughter(d)->pt() );
	vDauEta.push_back( (*genParticles_)[p].daughter(d)->eta() );
	vDauPhi.push_back( (*genParticles_)[p].daughter(d)->phi() );
	vDauE.push_back( (*genParticles_)[p].daughter(d)->energy() );
	nDau++;
      }
      
      nBranches_->genParticle_nDau  .push_back( nDau  );
      nBranches_->genParticle_nMoth .push_back( nMoth );      
      nBranches_->genParticle_mother.push_back( vMoth );
      nBranches_->genParticle_mother_pt.push_back( vMothPt );
      nBranches_->genParticle_mother_eta.push_back( vMothEta );
      nBranches_->genParticle_mother_phi.push_back( vMothPhi );
      nBranches_->genParticle_mother_e.push_back( vMothE );
      nBranches_->genParticle_dau   .push_back( vDau  );
      nBranches_->genParticle_dau_pt.push_back( vDauPt );
      nBranches_->genParticle_dau_eta.push_back( vDauEta );
      nBranches_->genParticle_dau_phi.push_back( vDauPhi );
      nBranches_->genParticle_dau_e.push_back( vDauE );

    }

    nBranches_->genParticle_N = nBranches_->genParticle_pt.size(); // save number of save genParticles
    
}

